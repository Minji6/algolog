def solution(myString):
    answer = ''
    for myStr in myString :
        if myStr == "a" or myStr=="A" : answer += "A"
        else : answer += myStr.lower()
    return answer