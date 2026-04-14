def solution(intStrs, k, s, l):
    answer = []
    
    for str1 in intStrs:
        str_num = ''
        for i in range(s, s + l):
            str_num = str_num + str1[i]
        num = 0
        num = int(str_num)
        if num > k:
            answer.append(num)
    
    return answer