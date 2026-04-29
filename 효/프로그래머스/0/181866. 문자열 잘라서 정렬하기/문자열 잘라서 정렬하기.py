def solution(myString):
    arr = myString.split("x")
    answer = []
    for i in arr:
        if i != "":
            answer.append(i)
    return sorted(answer)