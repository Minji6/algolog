def solution(num_list):
    answer = 0 
    num1 = 0
    num2 = 0
    for i in range(0, len(num_list)):
        if i % 2 == 0:
            num1 = num1 + num_list[i]
        if i % 2 == 1:
            num2 = num2 + num_list[i]
    
    if num1 >= num2:
        answer = num1
    else:
        answer = num2
    
    return answer