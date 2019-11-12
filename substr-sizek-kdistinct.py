from collections import Counter, defaultdict

def soln(s, k):
	N = len(s)
	res = set()

	if N < k:
		return []

	ctr = Counter(s[0 : k])
	for i in range(N - k + 1):
		if len(ctr) == k:
			res.add(s[i : i + k])

		if i < N - k:
			ctr[s[i]] -= 1
			if ctr[s[i]] == 0:
				del ctr[s[i]]

			ctr[s[i + k]] += 1

	return list(res)

print(soln('abcabc', 3))
print(soln('abacab', 3))
print(soln('awaglknagawunagwkwagl', 4))
