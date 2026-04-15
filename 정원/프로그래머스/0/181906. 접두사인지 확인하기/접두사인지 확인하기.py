def solution(my_string, is_prefix):
    answer = 0
    head = []
    for i in range(len(my_string)) :
        head.append(my_string[:i])
    if is_prefix in head :
        answer = 1
    return answer