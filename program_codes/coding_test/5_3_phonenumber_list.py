def solution(phone_book):
    phone_book.sort()

    for i in range(1,len(phone_book)):
        val = phone_book[i-1] 
        if val == phone_book[i][:len(val)]:
                return False  
    return True