def solution(my_string, queries):
    arr = list(my_string)
    for k in queries:
        (s, e) = k
        arr[s:e+1] = arr[s:e+1][::-1]
    return (''.join(arr))