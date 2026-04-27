def solution(strArr):
    answer = []
    for i in range(0, len(strArr)):
        if i % 2 == 0:
            a = strArr[i].lower()
            answer.append(a)
        if i % 2 == 1:
            a = strArr[i].upper()
            answer.append(a)
            
    return answer