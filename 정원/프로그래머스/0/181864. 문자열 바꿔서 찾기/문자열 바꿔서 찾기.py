def solution(myString, pat):
    answer = 0
    myStr = ''
    for k in myString :
        if k == 'A' : myStr += 'B'
        else : myStr += 'A'
    
    if pat in myStr : answer = 1
    return answer