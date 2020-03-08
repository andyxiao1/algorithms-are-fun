t = int(input())

for _ in range(t):
    n, p, k = [int(x) for x in input().split()]
    goods = [int(x) for x in input().split()]
    goods.sort()
    dp = [[0] * (p + 1) for _ in range(n)]

    # n rows and p + 1 columns
    # dp[i][j] = how many goods vasya can buy from subset a_i - a_n starting with j coins
    last = goods[-1]
    second_last = goods[-2]
    for i in range(p, -1, -1):
        if i < last:
            break
        dp[-1][i] = 1

    for i in range(p, -1, -1):
        if i < second_last:
            break
        dp[-2][i] = 1 if i < last else 2

    for i in range(n - 3, -1, -1):
        curr, next = goods[i], goods[i + 1]
        for j in range(p, curr - 1, -1):
            if j < curr:
                break
            elif j < next:
                dp[i][j] = 1
            else:
                dp[i][j] = max(2 + dp[i + 2][j - next],
                               1 + dp[i + 1][j - curr])
    print(dp[0][p])
