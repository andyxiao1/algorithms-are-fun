t = int(input())

for _ in range(t):
	n, s = [int(x) for x in input().split()]
	arr = [int(x) for x in input().split()]
	
	total = 0
	max_a, max_i = 0, 1
	
	for i, a in enumerate(arr):
		total += a

		if total > s:
			if i == 0:
				print(1)
			# elif total - max_a > s:
			# 	print(0)
			else:
				print(max_i if max_a > a else i + 1)
			break
		else:
			if a > max_a:
				max_a, max_i = a, i + 1
	else:
		print(0)
