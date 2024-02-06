class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        candys = [1 for _ in ratings]
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candys[i] = candys[i - 1] + 1 
            
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candys[i] = max(candys[i + 1] + 1, candys[i])
            
        
        return sum(candys)
            
