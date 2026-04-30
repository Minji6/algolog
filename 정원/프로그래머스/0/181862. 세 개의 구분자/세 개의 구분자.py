def solution(myStr):
    answer = []
    temp = ""
    
    for k in myStr :
        if k == 'a' or k == 'b' or k == 'c' :
            if len(temp) != 0 : answer.append(temp)
            temp = ""
        else :
            temp += k
    if len(temp) != 0 : answer.append(temp)
    if len(answer) == 0 : answer.append("EMPTY")
    return answer