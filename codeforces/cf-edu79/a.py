t = int(input())

for _ in range(t):
    r, g, b = [int(x) for x in input().split()]
    if r > (b + g + 1):
        print('No')
    elif b > (r + g + 1):
        print('No')
    elif g > (r + b + 1):
        print('No')
    else:
        print('Yes')