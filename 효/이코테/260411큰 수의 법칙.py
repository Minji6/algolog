n, m, k = map(int,input().split())
data = list(map(int,input().split()))
data.sort(reverse=True)
a = m // (k + 1)
b = m % (k + 1)
first = (a * k) + b
second = m - first
data[0]*first + data[1]*second