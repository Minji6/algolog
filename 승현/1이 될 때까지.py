# import sys

# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
N, K = map(int, input().split())

cnt = 0
while (True):
    if N == 1:
        answer = cnt
        break
    if N % K == 0:
        N = N // K
        cnt = cnt + 1
    
    else:
        N = N - 1
        cnt = cnt + 1

print(cnt)
