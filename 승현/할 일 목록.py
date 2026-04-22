def solution(todo_list, finished):
    answer = []
    for i in range(0, len(finished)):
        if finished[i] != True:
            answer.append(todo_list[i])
            
    return answer