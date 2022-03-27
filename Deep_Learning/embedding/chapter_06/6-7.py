'''
단어 임베딩 파인 튜닝 네트워크 그래프 생성 
make_word_embedding_graph를 호출할 때 tune = True로 설정하면 파인튜닝네트워크 학습용,
False로 설정하면 예측 모드로 그래프를 생성함
'''
def make_word_embedding_graph(num_labels, vocab_size, embedding_size, tune=False):
    ids_placeholder = tf.placeholder(tf.int32, [None, None], name="input_ids")
    input_lengths = tf.placeholder(tf.int32, [None], name="input_lengths")
    labels_placeholder = tf.placeholder(tf.int32, [None], name="label_ids")
    if tune:
        dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")
    else:
        dropout_keep_prob = tf.constant(1.0, dtype=tf.float32)
    We = tf.Variable(tf.constant(0.0, shape=[vocab_size, embedding_size]), trainable=True)
    embedding_placeholder = tf.placeholder(tf.float32, shape=[vocab_size, embedding_size])
    embed_init = We.assign(embedding_placeholder)
    # shape : [batch_size, unroll_steps, dimension]
    embedded_words = tf.nn.embedding_lookup(We, ids_placeholder)
    # input of fine tuning network
    features = tf.nn.dropout(embedded_words, dropout_keep_prob)
    # Bidirectional LSTM Layer
    lstm_cell_fw = tf.nn.rnn_cell.LSTMCell(num_units=embedding_size,
                                           cell_clip=5,
                                           proj_clip=5)
    lstm_cell_bw = tf.nn.rnn_cell.LSTMCell(num_units=embedding_size,
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
        return ids_placeholder, input_lengths, labels_placeholder, dropout_keep_prob, embedding_placeholder, embed_init, logits, loss
    else:
        # prob Layer
        probs = tf.nn.softmax(logits, axis=-1, name='probs')
        return ids_placeholder, input_lengths, labels_placeholder, probs