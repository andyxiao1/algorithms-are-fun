for r in range(5):
    for c, v in enumerate(map(int, input().split())):
        if v:
            print(abs(2 - r) + abs(2 - c))
