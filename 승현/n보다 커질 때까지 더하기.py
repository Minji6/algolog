def solution(numbers, n):
    answer = 0
    for i in range(0, len(numbers)):
        if answer <= n:
            answer = answer + numbers[i]
            
    return answer