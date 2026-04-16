def solution(n, k):
    answer = []
    m = (n // k)
    for i in range(k,n+1,k):
        answer.append(i)
    return answer