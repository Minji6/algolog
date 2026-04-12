def solution(a, b):
    answer = 0
    c = str(a) + str(b)
    c1 = int(c)
    d = 2 * a * b
    if c1 < d:
        answer = d
    elif c1 > d:
        answer = c1
    elif c1 == d:
        answer = c1
    return answer