def solution(array, commands):
    answer = []
    for n in commands:
        temp = array[n[0]-1:n[1]]
        temp.sort()
        answer.append(temp[n[2]-1])
        
        
    
    return answer

