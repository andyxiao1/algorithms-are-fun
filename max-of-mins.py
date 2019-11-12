def soln(M):

	# solve first row
	min_v = float('inf')
	for i in range(1, len(M[0])):
		min_v = min(M[0][i], min_v)
		M[0][i] = min_v

	# solve first col
	min_v = float('inf')
	for i in range(1, len(M)):
		min_v = min(M[i][0], min_v)
		M[i][0] = min_v

	for r in range(1, len(M)):
		for c in range(1, len(M[r])):
			M[r][c] = min(M[r][c], max(M[r - 1][c], M[r][c - 1]))

	return max(M[-2][-1], M[-1][-2])


print(soln([[5, 1], [4, 5]]))
print(soln([[1, 2, 3], [4, 5, 1]]))