N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 5 8 3
# 2 4 5 4 6

arr.sort()

a = arr[N - 1]
b = arr[N - 2]

ans = 0
ans_1 = 0
ans_2 = 0
ans_1 = M // (K + 1)
ans_2 = M % (K + 1)
ans = ans_1 * (3 * a + b) + ans_2 * b

print(ans)