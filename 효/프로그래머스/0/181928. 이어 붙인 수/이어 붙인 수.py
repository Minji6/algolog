def solution(num_list):
    answer1 = ""
    answer2 = ""
    for i in num_list:
        if i % 2 == 1:
            answer1 += str(i)
        else:
            answer2 += str(i)
    return int(answer1) + int(answer2)