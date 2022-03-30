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


''' 4. CPU 전체 정보 확인 '''
$ cat /proc/cpuinfo 

''' 5. CPU 코어 수 확인 ''' 
$ cat /proc/cpuinfo | grep processor | wc -l 

''' 6. 논리 코어 수 확인 ''' 
$ grep -c processeor /proc/cpuinfo 

''' 7. 물리 CPU 개수 ''' 
$ grep "physical id" /proc/cpuinfo | sort -u | wc -l

''' 8. CPU당 물리 코어 수 확인 ''' 
$ grep "cpu cores" /proc/cpuinfo | tail -1

''' 9. 우분투 그래픽 카드 GPU 확인 방법 '''
$ lspci | grep -i VGA
