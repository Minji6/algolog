def solution(my_string, queries):
    answer = ''
    for i in queries :
        s, e = i[0], i[1]
        temp = ''.join(reversed(my_string[s:e+1]))
        my_string = my_string[:s] + temp + my_string[e+1:]
        
    answer = my_string
    return answer