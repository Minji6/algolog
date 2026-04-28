def solution(myString, pat):
    result=''
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            result = myString[:i+len(pat)] 
    return result