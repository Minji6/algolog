def solution(arr, queries):
    answer = []
    
    for i in range(0, len(queries)):
        a = 0
        b = 0
        a = arr[queries[i][0]]
        b = arr[queries[i][1]]
        arr[queries[i][0]] = b
        arr[queries[i][1]] = a
        answer = arr
    
    return answer