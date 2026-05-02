N = input()
# [[0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0]]
arr = [[0] * 8 for _ in range(0, 8)]
change_num_arr = ["a", "b", "c", "d", "e", "f", "g", "h"]
n = N[0]
num_r = 0
num_c = 0
for i in range(0, len(change_num_arr)):
    if change_num_arr[i] == n:
        num_r = i

num_c = int(N[1]) - 1
# print(num_r, num_c)

for i in range(0, 8):
    for j in range(0, 8):
        if i == num_r and j == num_c:
            arr[i][j] = 1

# print(arr)

cnt = 0
dr = [-2, 0, 2, 0]
dc = [0, 2, 0, -2]
last_dr = [-1, 1]

for d in range(0, 4):
    nr = num_r + dr[d]
    nc = num_c + dc[d]
    if d % 2 == 0:
        for l in range(0, 2):
            nc = nc + last_dr[l]
            # print(nr, nc)
            if 0 <= nr < 8 and 0 <= nc < 8 and arr[nr][nc] == 0:
                cnt = cnt + 1
                arr[nr][nc] = 1
                # for p in arr:
                #     print(p)
    
                # print("//////////////////////////////")
            nc = nc - last_dr[l]

    else:
        for l in range(0, 2):
            nr = nr + last_dr[l]
            # print(nr, nc)
            if 0 <= nr < 8 and 0 <= nc < 8 and arr[nr][nc] == 0:
                cnt = cnt + 1
                arr[nr][nc] = 1
                # for p in arr:
                #     print(p)
                # print("//////////////////////////////")
            nr = nr - last_dr[l]

    nr = 0
    nc = 0
    
print(cnt)
