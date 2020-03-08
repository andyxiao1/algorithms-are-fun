n, *r1_arr = [int(x) for x in input().split()]
m, *p1_arr = [int(x) for x in input().split()]
k, *p2_arr = [int(x) for x in input().split()]
A, B = [int(x) for x in input().split()]

r1, p1, p2 = max(r1_arr), max(p1_arr), min(p2_arr)

print(((p1 * B * (r1 ** 2)) / (p2 * A + p1 * B)) ** .5)

