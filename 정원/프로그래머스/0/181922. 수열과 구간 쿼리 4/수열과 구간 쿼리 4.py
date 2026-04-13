def solution(arr, queries):
    for query in queries :
        for i in range(len(arr)) :
            if i >= query[0] and i <= query[1] :
                if i % query[2] == 0 :
                    arr[i] += 1
    answer = arr
    return answer