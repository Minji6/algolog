n,m = map(int, input().split())

answer = 0

for i in range(n):
    card = list(map(int, input().split()))
    min_card = min(card)
    answer = max(answer, min_card)

print(answer)