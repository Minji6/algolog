def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        n = str(i)
        cnt = 0
        for j in range(0, len(n)):
            if n[j] == "0" or n[j] == "5":
                cnt = cnt + 1
                
            if cnt == len(n):
                answer.append(int(n))
                
    if answer == []:
        answer.append(-1)
            
    
    return answer