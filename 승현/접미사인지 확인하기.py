def solution(my_string, is_suffix):
    answer = []
    ans = 0
    for i in range(0, len(my_string)):
        str1 = ''
        for j in range(i, len(my_string)):
            str1 = str1 + my_string[j]
        if str1 != '':
            answer.append(str1)
    for ans_str in answer:
        if ans_str == is_suffix:
            ans = 1
    
    return ans