class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        
        heapq.heapify(maxHeap)
        print(maxHeap)
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if first < second:
                print("hi")
                heapq.heappush(maxHeap, (first - second))

            
            print(maxHeap)
        maxHeap.append(0)
        return -maxHeap[0]