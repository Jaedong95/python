list = [4,3,2,1,8,7,5,10,11,16,21,6]

def bubble_sort(arr):
    length = len(arr) - 1
    
    for i in range(length):
        for j in range(length-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(list))