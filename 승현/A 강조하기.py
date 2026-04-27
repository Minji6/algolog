def solution(myString):
    answer = ''
    for a in myString:
        if a == "a":
            my_a = a.upper()
            answer = answer + my_a
        else:
            my_a = a.lower()
            answer = answer + my_a
        
            
    return answer