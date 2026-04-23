def solution(myString, pat):
    answer = 0
    myString = myString.upper()
    # print(myString)
    pat = pat.upper()
    # print(pat)
    for i in range(0, len(myString) - len(pat) + 1):
        if myString[i] == pat[0]:
            cnt = 1
            print(i)
            print(myString[i])
            for j in range(1, len(pat)):
                if myString[i + cnt] == pat[cnt]:
                    cnt = cnt + 1
            if cnt == len(pat):
                answer = 1
            
    return answer

# print(solution("AbCdEfG", "aBc" ))