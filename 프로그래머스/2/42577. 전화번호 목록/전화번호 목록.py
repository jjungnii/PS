def solution(phone_book): 
    dic = {} 
    for num in phone_book: 
        dic[num] = 1 
    
    for num in phone_book: 
        arr = "" 
        for elem in num: 
            arr += elem
            if arr in dic and arr != num:       
                return False 
                
    return True