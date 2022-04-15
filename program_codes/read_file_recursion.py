''' 폴더를 재귀적으로 탐색하여 파일 읽어들이기 ''' 
import os 

def read_folder(path):
    # 폴더의 요소 읽어 들이기 
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path+'/'+item)
        else:
            print('파일:',item)

read_folder('.')