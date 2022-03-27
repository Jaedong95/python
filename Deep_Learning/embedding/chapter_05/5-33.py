'''
멀티헤드 어텐션
'''
with tf.variable_scope('attention'):
    attention_heads = []
    with tf.variable_scope('self'):
        attention_head = attention_layer(
            from_tensor = layer_input, 
            to_tensor = layer_input, 
            attention_mask = attention_mask,
            num_attention_heads = num_attention_heads,
            size_per_head = attention_head_size, 
            attention_probs_dropout_prob = attention_probs_dropout_prob, 
            initializer_range=initializer_range,
            do_return_2d_tensor=True, 
            batch_size=batch_size,
            from_seq_length=seq_length, 
            to_seq_length=seq_length)
        attention_heads.append(attention_head)
    attention_output = None 
    if len(attention_heads) == 1: 
        attention_output = attention_head[0] 
    else:
        attention_output = tf.concat(attention_heads, axis=-1) 
    with tf.variabe_scope('output'):
        attention_output = tf.layers.dense(
            attention_output, 
            hidden_size, 
            kernel_initializer = create_initializer(initializer_range))
        attention_output = dropout(attention_output, hidden_dropout_prob)
        attention_output = layer_norm(attention_output + layer_input)