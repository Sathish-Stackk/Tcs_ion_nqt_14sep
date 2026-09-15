a, b, n = map(int, input().split(','))

series = [a, b]

for i in range(2, n):
    series.append(series[-1] + series[-2])

print(*series)
