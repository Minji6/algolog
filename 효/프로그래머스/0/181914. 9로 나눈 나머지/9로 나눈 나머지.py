def solution(number):
    answer = []
    list1 = list(map(int, number))
    return sum(list1) % 9
    