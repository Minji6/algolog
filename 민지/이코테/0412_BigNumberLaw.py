n, m, k = map(int,input().split())
arr = list(map(int,input().split()))

sort_arr = sorted(arr, reverse=True)

first = sort_arr[0]
second = sort_arr[1]

# int를 안하면 실수값이 나옴
count = int(m / (k+1)) * k
left = m % (k+1)
count += left

answer = 0
answer += count * first
answer += (m - count) * second

print(answer)