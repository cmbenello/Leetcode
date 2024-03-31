class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        
        def helper(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            
            if total > target or i >= len(candidates):
                return
            
            
            curr.append(candidates[i])
            
            helper(i, curr, total + candidates[i])
            
            curr.pop()
            
            helper(i + 1, curr, total)
            
        helper(0, [], 0)
        
        return res