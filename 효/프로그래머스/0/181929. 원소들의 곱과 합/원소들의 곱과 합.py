import math
def solution(num_list):
    m = math.prod(num_list)
    s = sum(num_list)
    if m > s**2:
        return 0
    else:
        return 1