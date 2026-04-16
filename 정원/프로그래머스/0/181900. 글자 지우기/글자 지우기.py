def solution(my_string, indices):
    answer = ''
    indices.sort(reverse=True)
    for i in (indices) :
        my_string = my_string[:i] + my_string[i+1:]
    answer = my_string
    return answer