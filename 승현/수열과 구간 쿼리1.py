def solution(arr, queries):
    answer = []
    for i in range(0, len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        for j in range(s, e + 1):
            arr[j] = arr[j] + 1
            
    answer = arr
    return answer