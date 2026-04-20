def solution(arr, intervals):
    answer = []
    for interval in intervals :
        answer = answer + arr[interval[0]:interval[1]+1]
    return answer