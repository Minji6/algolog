def solution(arr, query):
    answer = []
    for q in query:
        if q % 2 == 0:
            while len(arr) > q + 1:
                arr.pop()
                
        if q % 2 == 1:
            s = 0
            e = len(arr) - 1
            while s < e:
                arr[s], arr[e] = arr[e], arr[s]
                s = s + 1
                e = e - 1
                
            while len(arr) > q + 1:
                arr.pop()
                
            s = 0
            e = len(arr) - 1
            while s < e:
                arr[s], arr[e] = arr[e], arr[s]
                s = s + 1
                e = e - 1
            
    answer = arr
        
    return answer