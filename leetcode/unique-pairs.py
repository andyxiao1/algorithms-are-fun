def unique_pairs(nums, target):
	seen = set()
	res = set()

	for v in nums:
		tgt = target - v
		if tgt in seen:
			res.add((min(tgt, v), max(tgt, v)))
		seen.add(v)

	return len(res)

if __name__ == '__main__':
	print(unique_pairs([1, 1, 2, 45, 46, 46], 47))
	print(unique_pairs([1, 1], 2))
	print(unique_pairs([1, 5, 1, 5], 6))


'''
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
Example 2:

Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2
Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
'''