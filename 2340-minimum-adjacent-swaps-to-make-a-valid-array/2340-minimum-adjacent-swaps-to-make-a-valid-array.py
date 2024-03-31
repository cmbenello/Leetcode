class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        #Find the index of the earliest min and max the last max
        # Then just minus the length and then + 1 if they overlap

        max_val = max(nums)
        min_val = min(nums)
        
        max_index = nums[::-1].index(max_val)
        min_index = nums.index(min_val)
        
        
        res = 0
        
        if len(nums) - max_index - 1 < min_index:
            res -= 1
            
        res += max_index
        res += min_index
        
        return res