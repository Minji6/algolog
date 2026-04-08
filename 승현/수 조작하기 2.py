def solution(numLog):
    answer = ''
    for i in range(0, len(numLog)):
        if i == len(numLog) - 1:
            break
        if numLog[i] + 1 == numLog[i+1]:
            answer = answer + "w"
        if numLog[i] - 1 == numLog[i+1]:
            answer = answer + "s"
        if numLog[i] + 10 == numLog[i+1]:
            answer = answer + "d"
        if numLog[i] - 10 == numLog[i+1]:
            answer = answer + "a"
            
    
    return answer