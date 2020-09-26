import heapq
T = int(input())
res = []
for case in range(T):
    N = int(input())
    nums = [int(x) for x in input().split()]
    h = 0
    heap = []
    
    for i, n in enumerate(nums):
        if n > h:
            heapq.heappush(heap, n)
            if len(heap) >= h + 1:
                while heap and heap[0] <= h + 1:
                    heapq.heappop(heap)
                h += 1
        nums[i] = str(h)
    print('Case #{}: {}'.format(case + 1, ' '.join(nums)))
