import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(0, N)]
min_arr = []

for arr_1 in arr:
    arr_1.sort()
    min_arr.append(arr_1[0])
max_num = 0
for i in range(0, len(min_arr)):
    if min_arr[i] > max_num:
        max_num = min_arr[i]
# print(min_arr)
print(max_num)


