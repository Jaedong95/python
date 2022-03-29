'''
Tuner 클래스 (6)  - 입력 값 생성, tune 함수 
코드 6-1 ~ 6-5는 make_input과 tune 없이는 작동하지 x 
자식 클래스는 이 함수들을 구현해 반드시 오버라이드하도록 강제함
'''
def make_input(self, sentences, labels, is_training):
    '''
    입력값 생성 함수 오버라이드
    '''
    raise NotImplementedError

def tune(self):
    '''
    tune 함수 오버라이드
    '''
    raise NotImplementedError