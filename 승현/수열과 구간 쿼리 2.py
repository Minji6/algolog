def solution(arr, queries):
    answer = []
    
    for k in range(0, len(queries)):
        s = queries[k][0]
        e = queries[k][1]
        ans = 1000000
        for i in range(s, e + 1):
            if queries[k][2] < arr[i] < ans:
                ans = arr[i]
        if ans == 1000000:
            ans = -1
    
        answer.append(ans)
    
    return answer