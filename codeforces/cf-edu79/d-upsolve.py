n = int(input())
kids = [None] * n
total_possibilities = 0
valid_possibilities = 0

for i in range(n):
    kids[i] = {int(x) for i, x in enumerate(input().split()) if i > 0}
    total_possibilities += len(kids[i])
    valid_possibilities += len(kids[i])

total_possibilities *= n

for i in range(n - 1):
    for j in range(i + 1, n):
        valid_possibilities += len(kids[i] & kids[j])

print((valid_possibilities * total_possibilities ** 998244351) % 998244353 )