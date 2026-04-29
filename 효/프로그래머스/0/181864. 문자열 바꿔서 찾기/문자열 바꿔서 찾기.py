def solution(myString, pat):
    answer = "" 
    answer = myString.replace("A", "C").replace("B", "A").replace("C", "B")
    if pat in answer:
        return 1
    else:
        return 0
    