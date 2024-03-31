class Solution:
    def reorganizeString(self, s: str) -> str:
        # have a heap of all the values and then go through them in like a priority queue
        
        res = ""
        prev = "A"
        
        count = Counter(s)
        
        q = [(-cnt, char) for char, cnt in count.items()]
        
        heapq.heapify(q)
        print(q)
        while q:
            top = heapq.heappop(q)
            if top[1] == prev:
                copy = top
                if q:
                    top = heapq.heappop(q)
                else:
                    return ""
                heapq.heappush(q, copy)
            
            top = (top[0] + 1, top[1])
            if top[0] != 0:
                heapq.heappush(q, top)
            res += top[1]
            prev = top[1]
        
        
        
        return res