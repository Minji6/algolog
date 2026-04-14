def solution(my_string):
    answer = []
    
    for i in range(0, len(my_string)):
        str1 = ''
        for j in range(i, len(my_string)):
            str1 = str1 + my_string[j]
        if str1 != '':
            answer.append(str1)
    answer.sort()
    return answer