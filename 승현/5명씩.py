def solution(names):
    answer = []
    cnt = 0
    for i in range(0, len(names)):
        cnt = cnt + 1
        if cnt % 5 == 1:
            answer.append(names[i])
    
    return answer