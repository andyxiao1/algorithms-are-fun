def soln(nums, target):
	target -= 30
	max_pair = [0, 0]
	max_indices = [-1, -1]
	seen = {}

	for i, n in enumerate(nums):
		tgt = target - n
		if tgt in seen:
			pair = [min(tgt, n), max(tgt, n)]
			indices = [seen[tgt], i]

			if pair[1] > max_pair[1] or max_indices[0] == -1:
				max_pair = pair
				max_indices = indices
		else:
			seen[n] = i

	return max_indices


print(soln([1, 10, 25, 35, 60], 90))
print(soln([20, 50, 40, 25, 30, 10], 90))
