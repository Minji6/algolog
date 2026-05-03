def solution(pos) :
    pos = input()
    answer, a, b = 0, 1, 1

    # 이동 1
    if 98 < ord(pos[0]) < 103 : a += 1
    if 1 < int(pos[1]) < 8 : answer = a*2
    else : answer = a

    # 이동 2
    if 2 < int(pos[1]) < 7 : b += 1
    if 97 < ord(pos[0]) < 104 : answer += b*2
    else : answer += b

    return answer