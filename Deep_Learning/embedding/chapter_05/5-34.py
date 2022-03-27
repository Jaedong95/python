'''
Position-wise Feedforward Networks 
'''
with tf.variable_scope('intermediate'):
    intermediate_output = tf.layers.dense(
        attention_output, 
        intermediate_size, 
        activation = intermediate_act_fn,
        kernel_initializer=create_initializer(initializer_range))

with tf.variable_scope('output'):
    layer_output = tf.layers.dense(
        intermediate_output,
        hidden_size, 
        kernel_initalizer=create_initializer(initializer_range))
    layer_output = dropout(layer_output, hidden_dropout_prob)
    layer_output = layer_norm(layer_output + attention_output)