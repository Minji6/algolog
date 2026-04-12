def solution(n):
    answer1 = 0
    answer2 = 0
    if n % 2 == 1:
        for i in range(1,n+1,2):
            answer1 += i
        return answer1
    else:
        for i in range(2,n+1,2):
            answer2 += i*i
        return answer2