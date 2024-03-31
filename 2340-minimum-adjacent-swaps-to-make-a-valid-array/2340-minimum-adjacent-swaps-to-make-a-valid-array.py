class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        #Find the index of the earliest min and max the last max
        # Then just minus the length and then + 1 if they overlap

        
        max_val = -1
        min_val = float('inf')
        
        
        for i in range(len(nums)):
            if nums[i] >= max_val:
                max_val = nums[i]
                max_index = i
            
            if nums[i] < min_val:
                min_val = nums[i]
                min_index = i
            
        
        res = 0
        
        if max_index < min_index:
            res -= 1
        
        res += len(nums) - max_index - 1
        res += min_index
        
        return res