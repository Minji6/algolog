def solution(myString):
    answer = myString.split("x")
    answer1 = []
    for i in answer:
        answer1.append(len(i))
    return answer1