def solution(str_list):
    answer = []
    num = 0
    cnt = 0
    for i in range(0, len(str_list)):
        if str_list[i] == "l":
            num = 1
            cnt = i
            break
        if str_list[i] == "r":
            num = -1
            cnt = i
            break
            
    if num == 1:
        for j in range(0, cnt):
            answer.append(str_list[j])
            # print(cnt)
            # print(answer)
            
    
    if num == -1:
        for j in range(cnt + 1, len(str_list)):
            answer.append(str_list[j])
            
    return answer