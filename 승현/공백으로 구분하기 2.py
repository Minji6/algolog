def solution(my_string):
    answer = []
    ans = ""
    for i in range(0, len(my_string)):
        
        if my_string[i] == " " and ans != "":
            answer.append(ans)
            ans = ""
              
        if my_string[i] != " ":
            ans = ans + my_string[i]
        
        if i == len(my_string) - 1 and ans != "":
            answer.append(ans)
        
    return answer