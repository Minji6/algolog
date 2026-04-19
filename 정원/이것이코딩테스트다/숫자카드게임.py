# 배열 크기 입력 받고 초기화
N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]

# 행단위로 입력받기
print(M,"개씩",N,"번입력")
for i in range(N):
    arr[i] = list(map(int, input().split()))

# i번째 행과 i+1번째 행의 최솟값 중의 더 큰 값을 저장
res = 0
for i in range(N-1) :
    res = max(min(arr[i]), min(arr[i+1]))

print(res)
    