''' 1. 사용 가능 GPU 조회 '''
import tensorflow as tf 

with tf.device('/gpu:0'):
    sess = tf.compat.v1.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))

print(tf.config.list_physical_devices('GPU')) 


''' 2. 사용 가능 GPU 조회 '''
import tensorflow as tf 

strategy = tf.distribute.MirroredStrategy()
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))

''' 3. 사용 가능 GPU 조회 '''
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())
