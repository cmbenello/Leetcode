class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        heapq.heapify(dists)
        
        
        for point in points:
            dist = float((point[0] * point[0] + point[1] * point[1]))
            dist = math.sqrt(dist)
            heapq.heappush(dists, [-dist, point])
            if len(dists) > k:
                temp = heapq.heappop(dists)

        res = [point for [dist, point] in dists]
        return res