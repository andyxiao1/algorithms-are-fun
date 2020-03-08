t = int(input())

for _ in range(t):
    a, b, c, r = [int(x) for x in input().split()]
    a, b = min(a, b), max(a, b)
    res = b - a - (max(min(b, c + r), a) - min(max(a, c - r), b))
    print(res)
