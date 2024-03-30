class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        temp = sorted(count.items(), key = lambda x: x[1])[::-1]
        
        res = []
        
        for i in range(k):
            res.append(temp[i][0])
            
        return res