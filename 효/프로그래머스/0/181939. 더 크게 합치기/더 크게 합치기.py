def solution(a, b):
    answer = 0
    a1 = str(a)
    b1 = str(b)
    c = a1 + b1 
    d = b1 + a1
    if c < d:
        answer = int(d)
    else:
        answer = int(c) 
    return answer