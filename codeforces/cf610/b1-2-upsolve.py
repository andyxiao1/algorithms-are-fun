# in competition approach: timed out
    # n rows and p + 1 columns
    # dp[i][j] = how many goods vasya can buy from subset a_i - a_n starting with j coins

# better approach
    # array of size n
    # dp[i] is cheapest cost to buy first i + 1 goods
    # base case: for all j in first k -> dp[j] = a_j + a_j-1
    # return i + 1 of largest dp[i] <= p

for j in range(int(input())):
    n, p, k = [int(x) for x in input().split()]
    goods = [int(x) for x in input().split()]
    goods.sort()

    dp = [0] * n
    dp[0] = goods[0]

    if dp[0] > p:
        print(0)
        continue

    for i in range(1, k - 1):
        dp[i] = goods[i] + dp[i - 1]

    for i in range(k - 1, n):
        dp[i] = goods[i] + min(dp[i - 1], dp[i - k])

    res = 0
    for i in range(0, n):
        if dp[i] <= p:
            res = i + 1
    print(res)

