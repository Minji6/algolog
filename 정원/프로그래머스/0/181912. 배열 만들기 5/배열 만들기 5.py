def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs :
        ret = int(intStr[s:s+l])
        if ret > k :
            answer.append(ret)
    return answer