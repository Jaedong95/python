''' 네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 
    이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 
    한다. 
    
    1. 지도는 한 변의 길이가 n인 정사각형 배열로, 각 칸은 "공백(' ')" 또는 "벽('#')"
       두 종류로 이루어져 있다. 
    2. 전체 지도는 두 장의 지도를 겹쳐 얻을 수 있다. 지도 1 또는 지도 2 중 어느 
       하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인
       부분은 전체 지도에서도 공백이다. 
    3. '지도 1'과 '지도 2'는 각각 정수 배열로 암호화되어 있다. 
    4. 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화 했을 
       때얻어지는 이진수에 해당하는 값의 배열이다. 
       
    01001(2) = 9, 10100(2) = 20, 11100(2) = 28, 10010(2) = 18, 01011(2) = 11 
    11110(2) = 30, 00001(2) = 2, 10101(2) = 21, 10001(2) = 17, 11100(2) = 28 

    네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 프로그램 작성
    (원래의 비밀지도를 해석하여 '#', 공백으로 구성된 문자열 배열로 출력)

    * 입력으로 지도의 한 변 크기 n, 2개의 정수 배열 arr1, arr2가 들어옴 
      1 <= n <= 16. 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하 '''  

''' 나의 풀이 -> 실패 .. 2진수로 변환 시 01101 -> 1101로 출력되어 들쭉날쭉.. 해결 실패 '''
def solution(n, arr1, arr2):
    answer = []
    b_arr1 = []; b_arr2 = []
    
    for i in range(n):
        b_arr1.append([bin(arr1[i])[2:]])
        b_arr2.append([bin(arr2[i])[2:]])    
            
    for i in range(n):
        if len(b_arr1[i]) != n:
            for j in range(n - len(b_arr1[i])):
                b_arr1[i].insert(j, '0')
    
    print(b_arr1)
    # for i in range(n):
    
    return answer 

''' 모범 답안 -> rjust 사용 '''
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

''' 모범 답안2 -> 정규식 사용 '''
import re 

def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer