def solution(num_list):
    answer = []
    answer = num_list
    i = len(num_list)
    if num_list[i - 1] > num_list[i-2]:
        answer = answer + [num_list[i - 1] - num_list[i - 2]]
    if num_list[i - 1] <= num_list[i - 2]:
        answer = answer + [num_list[i - 1] * 2]
        
    return answer
    