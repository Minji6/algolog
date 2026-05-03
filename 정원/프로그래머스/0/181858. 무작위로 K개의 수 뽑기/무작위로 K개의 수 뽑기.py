def solution(arr, k):
    answer = []
    # arr = [200, 999, 1, 3, 500, 3, 200] 
    # mylist = list(set(arr))
    mylist = list(dict.fromkeys(arr))
    # print(mylist)
    # mylist.sort()
    
    if len(mylist) > k :
        answer = mylist[:k]
    elif len(mylist) < k :
        answer = mylist
        answer.extend([-1] * (k-len(mylist)))
    else : answer = mylist
        
    return answer