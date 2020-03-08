class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [] # max heap
        
        for i in range(K):
            p = points[i]
            dist = math.sqrt(p[0] ** 2 + p[1] ** 2)
            heapq.heappush(heap, (-dist, p))
        
        for i in range(K, len(points)):
            p = points[i]
            dist = math.sqrt(p[0] ** 2 + p[1] ** 2)
            if dist < -heap[0][0]:
                heapq.heapreplace(heap, (-dist, p))
        
        return [h[1] for h in heap]



class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # find k + 1^th smallest
        
        if not points or not K:
            return []
        
        l, r = 0, len(points) - 1
        
        def partition(l, r, p):
            # > r -> >= p
            points[p], points[r] = points[r], points[p]
            p = r
            r -= 1
            pivot_dist = math.sqrt(points[p][0] ** 2 + points[p][1] ** 2)

            while l <= r:
                dist = math.sqrt(points[l][0] ** 2 + points[l][1] ** 2)
                if dist < pivot_dist:
                    l += 1
                else:
                    points[l], points[r] = points[r], points[l]
                    r -= 1

            points[p], points[l] = points[l], points[p]
            return l

        while l <= r:
            p = random.randint(l, r)
            rank = partition(l, r, p)
            
            if rank == K - 1:
                return points[:K]
            elif rank > K - 1:
                r = rank - 1
            else:
                l = rank + 1
        
        return points[:r]