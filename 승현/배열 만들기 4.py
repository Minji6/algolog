def solution(arr):
    stk = []
    i = 0
    while(True):
        # print(stk)
        # print("i:", i)
        if i >= len(arr):
            break
        if len(stk) == 0:
            stk.append(arr[i])
            i = i + 1
        elif len(stk) != 0 and stk[len(stk)-1] < arr[i]:
            stk.append(arr[i])
            i = i + 1
        elif len(stk) != 0 and stk[len(stk) - 1] >= arr[i]:
            stk.pop()
        
    return stk