def solution(num_list):
    answer = 0
    cnt = 0
    for i in range(0, len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
        cnt = cnt + 1
    if answer == 0 and cnt != 0:
        answer = -1
        
    return answer