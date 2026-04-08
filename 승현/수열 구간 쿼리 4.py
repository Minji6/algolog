def solution(arr, queries):
    answer = []
    
    for k in range(0, len(queries)):
        s = queries[k][0]
        e = queries[k][1]

        for i in range(s, e + 1):
            if i % queries[k][2] == 0:
                arr[i] = arr[i] + 1

    answer = arr
        
    return answer