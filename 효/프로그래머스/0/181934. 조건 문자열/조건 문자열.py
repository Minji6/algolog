def solution(ineq, eq, n, m):
    answer = ""
    if ineq + eq == ">=":
        if (n >= m) == True:
            answer = 1
        else:
            answer = 0
        return answer
    elif ineq + eq == "<=":
        if (n <= m) == True:
            answer = 1
        else:
            answer = 0
    elif ineq + eq == ">!":
        if (n > m) == True:
            answer = 1
        else:
            answer = 0
    elif ineq + eq == "<!":
        if (n < m) == True:
            answer = 1
        else:
            answer = 0
    return answer