def solution(a, b, c, d):
    answer = [a,b,c,d]
    answer.sort(reverse=True)
    
    a, b, c, d = answer
    l1 = len(set(answer))
    if l1 == 1:
        answer = 1111*a
    elif l1 == 2:
        print()
        if a == b == c:
            answer = (10 * a + d)**2
        elif b == c == d:
            answer = (10 * d + a)**2
        else:
            answer = (a + d) * abs(a - d)
    elif l1 == 3:
        if a == b:
            answer = c * d
        elif b == c:
            answer = a * d
        elif c == d:
            answer = a * b
    else:
        answer = min(answer)
    return answer  
        
