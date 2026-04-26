def solution(arr):
    answer = list(arr)
    for i in range(len(answer)):
        if answer[i] >= 50 and answer[i] % 2 == 0:
            answer[i] = answer[i] // 2
        elif answer[i] < 50 and answer[i] % 2 == 1:
            answer[i] = answer[i] * 2
    return answer