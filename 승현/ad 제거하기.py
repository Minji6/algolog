def solution(strArr):
    print("strArr: ", strArr)
    answer = []
    ans = []
    pat = "ad"
    
    idx = 0
    for myString in strArr:
        for i in range(0, len(myString) - len(pat) + 1):
            if myString[i] == pat[0]:
                # print("i", i)
                cnt = 0
    
                for j in range(1, len(pat)):
                    if myString[i + j] == pat[j]:
                        cnt = cnt + 1

                if cnt == len(pat) - 1:
                    ans.append(idx)
                print("ans: ", ans)
        idx = idx + 1


    for i in range(0, len(strArr)):
        cnt = 0
        for j in range(0, len(ans)):
            if i == ans[j]:
                # print("아아아아악", i)
                cnt = cnt + 1
        if cnt == 0:
            answer.append(strArr[i])
            
    return answer