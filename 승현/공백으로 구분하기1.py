def solution(my_string):
    answer = []
    ans = ""
    for i in range(0, len(my_string)):
        
        if my_string[i] == " ":
            answer.append(ans)
            ans = ""
            continue
            
        ans = ans + my_string[i]
        
        if i == len(my_string) - 1:
            answer.append(ans)
        
    return answer