''' Q1. 리스트 평탄화.. 중첩된 리스트가 있을 때 중첩을 
    모두 제거하고 풀어서 1차원 리스트로 만드는 문제 (coding by 강사님)  '''
def flatten(data):
    output = []
    if type(data) != list:
        return output.append(data)
    else:
        for element in data:
            # print(element)
            output += flatten(element)
    

example = [[1,2,3], [4, [5,6]], [7,[8, 9]]]

print('원본:',example)
print('변환:',flatten(example))

''' Q1. 리스트 평탄화, 리스트의 데이터가 리스트인지 아닌지 구분 필요'''
def flatten(data):
    output = [] 
    for element in data:
        if type(element) == list:
            output += flatten(element)
        else:
            output.append(element)
        
    return output 

example = [[1, 2, 3] [4, [5, 6]], 7, [8, 9]]
print('원본:', example)
print('변환:', flatten(example))