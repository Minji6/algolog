def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        for i in range(0, len(num_list)):
            answer = answer + num_list[i]
    else:
        answer = 1
        for i in range(0, len(num_list)):
            answer = answer * num_list[i]    
    
    return answer