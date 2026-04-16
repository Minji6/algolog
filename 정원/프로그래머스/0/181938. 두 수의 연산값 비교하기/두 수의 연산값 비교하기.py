def solution(a, b):
    answer = 0
    temp1 = int(str(a) + str(b))
    temp2 = 2 * a * b
    answer = max(temp1, temp2)
    return answer