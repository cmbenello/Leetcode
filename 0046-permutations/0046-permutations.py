class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
        
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    helper(curr)
                    curr.pop()
            
        
        helper([])
        return res
                
        