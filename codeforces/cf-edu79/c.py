t = int(input())

for _ in range(t):
	n, m = map(int, input().split())
	stack = [int(x) for x in input().split()]
	order = [int(x) for x in input().split()]

	seen = set()
	res = 0
	stack_ptr = 0

	for present in order:
		if present in seen:
			res += 1
			seen.remove(present)
		else:
			k = len(seen)

			while stack[stack_ptr] != present:
				seen.add(stack[stack_ptr])
				k += 1
				stack_ptr += 1
			stack_ptr += 1
			res += 2 * k + 1
	print(res)

