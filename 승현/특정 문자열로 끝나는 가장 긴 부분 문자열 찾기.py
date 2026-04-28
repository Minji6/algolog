def solution(myString, pat):
    answer = ''
    ans = 0
    for i in range(0, len(myString) - len(pat) + 1):
        if myString[i] == pat[0]:
            cnt = 0
            for j in range(1, len(pat)):
                if myString[i + j] == pat[j]:
                    cnt = cnt + 1
            if cnt == len(pat) - 1:
                ans = i
    for i in range(0, ans + len(pat)):
        answer = answer + myString[i]
        
    return answer