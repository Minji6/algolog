def solution(num_list):
    answer = 0
    num = 0
    while (True):
        for i in range(0, len(num_list)):
            if num_list[i] % 2 == 0 and num_list[i] != 1:
                num_list[i] = num_list[i] // 2
                num = num + 1
            elif num_list[i] % 2 == 1 and num_list[i] != 1:
                num_list[i] = (num_list[i] - 1) // 2
                num = num + 1
                
        cnt = 0    
        for i in range(0, len(num_list)):
            if num_list[i] == 1:
                cnt = cnt + 1
                
        if cnt == len(num_list):
            answer = num
            return answer
        
        
        
    