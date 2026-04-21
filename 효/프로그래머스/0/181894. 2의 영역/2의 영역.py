def solution(arr):
    first = -1 
    second = -1
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            if first == -1:
                first = i
            second = i
    if first == -1:
        return [-1] 
    else:
        return arr[first:second+1]
    
            
            

        