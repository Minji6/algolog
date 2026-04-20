def solution(arr):
    answer = []
    idx = []
    for i in range (len(arr)) :
        if arr[i] == 2 : 
            idx.append(i)
    if len(idx) > 0:
        answer = arr[min(idx):max(idx)+1]
    else : answer.append(-1)
    
    return answer