n, k = map(int, input().split())

count = 0
while True:
    if n % k != 0:
        count += (n % k)
        n = n - (n % k)
    else:
        n = n // k
        count += 1

    if n == 1:
        break

print(count)