import re 

def funcReplacement(str):
    '''
    특수 문자 및 연속된 공백 제거하는 함수 
    '''
    # 특수문자 치환 
    tmp = re.sub(re.compile(\(|\)|,|\+|-|/|=|\*|\'|\"|\n|\.", re.DOTALL), " ", str)
    
    # 연속된 공백 제거 
    tmp = re.sub(re.compile(" [] {1, }", re.DOTALL), " ", tmp)
    return tmp 
    
    