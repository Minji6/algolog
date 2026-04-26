def solution(num_list):
    answer = list(num_list)
    count = 0
    for i in range(len(answer)):
        while answer[i] != 1:
            if answer[i] % 2 == 0:
                answer[i] = answer[i] // 2
                count += 1
            else:
                answer[i] = (answer[i] - 1) // 2
                count += 1
    return count