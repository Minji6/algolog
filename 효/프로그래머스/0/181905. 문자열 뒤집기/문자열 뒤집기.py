def solution(my_string, s, e):
    a = my_string[:s] 
    b = ''
    b += (my_string[s:e+1])
    b = b[::-1]
    c = my_string[e+1:]
    return a + b + c
    