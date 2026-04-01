N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# N, M, K = 5 8 3
# arr = [2, 4, 5, 4, 6]
# 5 8 3
# 2 4 5 4 6

num1 = 0
num2 = 0
num1_inx = 0

for i in range(0, N):
    if arr[i] >= num1:
        num1 = arr[i]
        num1_inx = i

# print(num1)
for i in range(0, N):

    if arr[i] > num2:
        if num1_inx != i and num1 == arr[i]:
            num2 = num1
            break
        if arr[i] == num1 and num1_inx == i:
            continue
        
        num2 = arr[i]
        # print(num2)

# print(num2)
ans = 0
a = M // (K + 1)
b = M % (K + 1)
# print(a)
# print(b)
ans =  (K * num1 * a) + (num2 * a) + (num1 * b)
print(ans)

