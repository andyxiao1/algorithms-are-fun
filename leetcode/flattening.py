from collections import Counter

for T in range(int(input())):
    N, K = [int(x) for x in input().split(' ')]
    arr = [int(x) for x in input().split(' ')]
    c = [[None] * N for _ in range(N)]
    K += 1 

    # calc cost of each i, j st i <= j - O(n^2)
    for i in range(N):
        for j in range(i, N):
            c[i][j] = (j - i + 1) - Counter(arr[i : j + 1]).most_common(1)[0][1]
            
    # DP bottom up solve for F(N, K) - O(n^2 * k)
    M = [[None] * K for _ in range(N)]

    for i in c:
      print(i)

    for row in range(N):
        M[row][0] = c[0][row]
    
    M[0] = [0] * K

    for i in range(1, K):
        for j in range(1, N):
            min_val = float('inf')
            for p in range(0, j):
                val = c[p + 1][j] + M[p][i - 1]
                min_val = min(val, min_val)
            M[j][i] = min_val
    
    res = M[N - 1][K - 1]
        
    for i in M:
      print(i)

    print('Case ' + str(T + 1) + ': ' + str(res))
