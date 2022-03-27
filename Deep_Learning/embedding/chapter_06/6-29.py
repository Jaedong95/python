'''
BERT 파인 튜닝 네트워크의 텐서 그래프 구축 
'''
def make_bert_graph(bert_config, max_seq_length, dropout_keep_prob_rate, num_labels, tune=False):
    '''
    BERT 모델의 입력값을 받는 텐서를 차례로 정의하고, 이들을 인자로 하는 BERT 모델을 
    호출해 BERT 모델의 텐서 그래프 구축 
    '''
    input_ids = tf.placeholder(tf.int32, [None, max_seq_length], name='inputs_ids')
    input_mask = tf.placeholder(tf.int32, [None, max_seq_length], name='input_mask')
    segment_ids = tf.placeholder(tf.int32, [None, max_seq_length], name='segment_ids')
    model = BertModel(config=bert_config,
                      is_training=tune,
                      input_ids=input_ids,
                      input_mask=input_mask,
                      token_type_ids=segment_ids)
    if tune:   # 학습 과정 
        # model.pooled_output: BERT 모델 마지막 레이어의 [CLS] 벡터 
        # 해당 벡터에 풀 커넥티드 레이어를 적용해 로짓 벡터 생성 
        bert_embeddings_dropout = tf.nn.dropout(model.pooled_output, keep_prob=(1 - dropout_keep_prob_rate))
        label_ids = tf.placeholder(tf.int32, [None], name='label_ids')
    else:   # 예측 과정 
        bert_embeddings_dropout = model.pooled_output 
        label_ids = None
    logits = tf.contrib.layers.fully_connected(inputs=bert_embeddings_dropout,
                                               num_outputs=num_labels,
                                               activation_fn=None,
                                               weights_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                               biases_initializer=tf.zeros_initializer())
    if tune:
        # loss layer
        CE = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=label_ids, logits=logits)
        loss = tf.reduce_mean(CE)
        return input_ids, input_mask, segment_ids, label_ids, logits, loss
    else:
        # prob layer
        probs = tf.nn.softmax(logits, axis=-1, name='probs')
        return model, input_ids, input_mask, segment_ids, probs