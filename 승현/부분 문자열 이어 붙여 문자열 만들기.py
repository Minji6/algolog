def solution(my_strings, parts):
    answer = ''

    for i in range(0, len(my_strings)):
        s = parts[i][0]
        e = parts[i][1]
        for j in range(s, e + 1):
            answer = answer + my_strings[i][j]
        
    return answer