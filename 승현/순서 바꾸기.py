def solution(num_list, n):
    answer = []
    lst1 = []
    lst2 = []
    for i in range(0, n):
        lst1.append(num_list[i])
        
    for i in range(n, len(num_list)):
        lst2.append(num_list[i])
    
    for i in range(0, len(lst2)):
        answer.append(lst2[i])
    
    for i in range(0, len(lst1)):
        answer.append(lst1[i])
    
    return answer