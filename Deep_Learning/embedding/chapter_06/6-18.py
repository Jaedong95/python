'''
ELMo 파인튜닝 네트워크의 텐서 그래프 구축 
'''
def make_elmo_graph(options_fname, pretrain_model_fname, max_characters_per_token, num_labels, tune=False):
    """
        ids_placeholder : ELMo 네트워크의 입력값 (ids)
            - shape : [batch_size, unroll_steps, max_character_byte_length]
        elmo_embeddings : fine tuning 네트워크의 입력값 (ELMo 네트워크의 출력값)
            - shape : [batch_size, unroll_steps, dimension]
        labels_placeholder : fine tuning 네트워크의 출력값 (예 : 긍정=1/부정=0)
            - shape : [batch_size]
        loss : fine tuning 네트워크의 loss
    """
    # BidirectionalLanguageModel(): 문자 수준 컨볼루션 신경망, 양방향 LSTM 레이어에 해당하는 
    #                               텐서플로 계산 그래프 생성, 프리트레인된 학습 파라미터 로드
    bilm = BidirectionalLanguageModel(options_fname, pretrain_model_fname)
    # Input placeholders to the biLM.
    ids_placeholder = tf.placeholder(tf.int32, shape=(None, None, max_characters_per_token), name='input')
    if tune:
        # Output placeholders to the fine-tuned Net.
        labels_placeholder = tf.placeholder(tf.int32, shape=(None))
    else:
        labels_placeholder = None
    # Get ops to compute the LM embeddings.
    embeddings_op = bilm(ids_placeholder)
    # Get lengths.
    input_lengths = embeddings_op['lengths']
    # define dropout
    if tune:
        dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")
    else:
        dropout_keep_prob = tf.constant(1.0, dtype=tf.float32)
    # the ELMo layer
    # 가중치를 곱해 가중합 수행  -> ELMo 임베딩 얻을 수 있음 
    # weight layers에 적용되는 가중치들: 파인 튜닝을 하며 다른 학습 파라미터들과 함께 업데이트 됨
    elmo_embeddings = weight_layers("elmo_embeddings",
                                    embeddings_op,
                                    l2_coef=0.0,
                                    use_top_only=False,
                                    do_layer_norm=True)
    # input of fine tuning network
    features = tf.nn.dropout(elmo_embeddings['weighted_op'], dropout_keep_prob)
    # Bidirectional LSTM Layer
    lstm_cell_fw = tf.nn.rnn_cell.LSTMCell(num_units=512,
                                           cell_clip=5,
                                           proj_clip=5)
    lstm_cell_bw = tf.nn.rnn_cell.LSTMCell(num_units=512,
                                           cell_clip=5,
                                           proj_clip=5)
    lstm_output, _ = tf.nn.bidirectional_dynamic_rnn(cell_fw=lstm_cell_fw,
                                                     cell_bw=lstm_cell_bw,
                                                     inputs=features,
                                                     sequence_length=input_lengths,
                                                     dtype=tf.float32)

    # Attention Layer
    output_fw, output_bw = lstm_output
    H = tf.contrib.layers.fully_connected(inputs=output_fw + output_bw, num_outputs=256, activation_fn=tf.nn.tanh)
    attention_score = tf.nn.softmax(tf.contrib.layers.fully_connected(inputs=H, num_outputs=1, activation_fn=None), axis=1)
    attention_output = tf.squeeze(tf.matmul(tf.transpose(H, perm=[0, 2, 1]), attention_score), axis=-1)
    layer_output = tf.nn.dropout(attention_output, dropout_keep_prob)

    # Feed-Forward Layer
    fc = tf.contrib.layers.fully_connected(inputs=layer_output,
                                           num_outputs=512,
                                           activation_fn=tf.nn.relu,
                                           weights_initializer=tf.contrib.layers.xavier_initializer(),
                                           biases_initializer=tf.zeros_initializer())
    features_drop = tf.nn.dropout(fc, dropout_keep_prob)
    logits = tf.contrib.layers.fully_connected(inputs=features_drop,
                                               num_outputs=num_labels,
                                               activation_fn=None,
                                               weights_initializer=tf.contrib.layers.xavier_initializer(),
                                               biases_initializer=tf.zeros_initializer())
    if tune:
        # Loss Layer
        CE = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels_placeholder, logits=logits)
        loss = tf.reduce_mean(CE)
        return ids_placeholder, labels_placeholder, dropout_keep_prob, logits, loss
    else:
        # prob Layer
        probs = tf.nn.softmax(logits, axis=-1, name='probs')
        return ids_placeholder, elmo_embeddings, probs