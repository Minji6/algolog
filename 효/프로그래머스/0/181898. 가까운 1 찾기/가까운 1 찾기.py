def solution(arr, idx):
    result = 0
    answer = idx
    while(idx < len(arr)):
        if arr[idx] != 1:
            idx += 1
            result += 1
        else:
            return idx
    return -1
    