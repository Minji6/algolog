def solution(n, control):
    answer = 0
    for i in control:
        if i == "w":
            n = n + 1
        if i == "s":
            n = n - 1
        if i == "d":
            n = n + 10
        if i == "a":
            n = n - 10
    answer = n
    
    return answer