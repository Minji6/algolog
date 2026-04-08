def solution(n):
    answer = []
    
    while (True):
        answer.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
            
        elif n % 2 == 1:
            n = (3 * n) + 1
            
            
    return answer