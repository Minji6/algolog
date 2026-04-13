N, M, K = map(int,input().split())
arr = list(map(int,input().split()))
i, j, res = 0, 0, 0
max1 = max(arr)
arr.remove(max1)
max2 = max(arr)

while i < 8 :
    if j < K :
        max_num = max1
        j += 1
    else :
        max_num = max2
        j = 0
    res += max_num
    i += 1

print(res)
