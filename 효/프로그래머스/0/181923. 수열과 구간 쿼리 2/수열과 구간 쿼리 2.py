def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        answer1 = []
        for i in range(s, e+1):
            if arr[i] > k:
                answer1.append((arr[i]))
        if answer1 == []:
            answer.append(-1)
        else:
            answer.append(min(answer1))
    return answer