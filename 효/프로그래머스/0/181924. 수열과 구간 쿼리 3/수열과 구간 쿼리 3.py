def solution(arr, queries):
    answer = []
    for k in queries:
        (i,j) = k
        arr[i], arr[j] = arr[j], arr[i]
    return arr