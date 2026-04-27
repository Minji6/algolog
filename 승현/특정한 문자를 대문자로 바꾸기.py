def solution(my_string, alp):
    answer = ''
    for i in range(0, len(my_string)):
        if my_string[i] == alp:
            a = my_string[i].upper()
            answer = answer + a
        else:
            answer = answer + my_string[i]
            
    return answer