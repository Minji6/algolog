def solution(num_list):
    answer = 0
    # 2, 4, 8, 16, 32... 2의 n승
    for num in num_list :
        if num == 1 : continue
        elif num < 4 : answer += 1
        elif num < 8 : answer += 2
        elif num < 16 : answer += 3
        else : answer += 4
    return answer