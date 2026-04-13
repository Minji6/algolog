def solution(a, b, c, d):
    answer = 0
    
    numlist = [a,b,c,d]
    numlist.sort()
    numset = set(numlist)
    
    
    # 4개 값이 전부 같은 경우
    if len(numset) == 1 :
        answer=a*1000+a*100+a*10+a
        
    # 4개 값이 전부 다른 경우
    elif len(numset) == 4 :
        answer = min(numset)
        
    # 2개, 2개인 경우
    elif len(numset) == 2 and numlist.count(a) == 2 :
        p,q = numset.pop(),numset.pop()
        answer = (p+q) * abs(p-q)
        
    # 3개, 1개인 경우
    elif len(numset)==2 and numlist.count(a) + numlist.count(b) > 3 :
        for i in numset : 
            if numlist.count(i) == 3:
                p = i
            else :
                q = i
        answer = (10*p+q) **2
    
    # 2개, 1개, 1개인 경우
    else :
        # 2개인 요소 찾기
        for i in numset :
            if numlist.count(i) == 2 :
                p = i
                break
        # 2개인 요소 삭제
        numset.remove(p)
        # 1개인 요소만 저장해서 연산
        q,r = numset.pop(), numset.pop()
        answer = q * r
        
    return answer