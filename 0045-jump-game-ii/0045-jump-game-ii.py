class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        pos = 0
        n = len(nums) - 1
        
        while pos < n:
            max_jump = 0
            max_jump_pos = 0
            res += 1 
            for i in range(1,nums[pos] + 1):
                if pos + i == n:
                    return res
                print(nums[pos + i] , end = " ")
                print(nums[pos + i] - nums[pos] + i, max_jump)
                if nums[pos + i] - nums[pos] + i > max_jump:
                    max_jump = nums[pos + i] - nums[pos] + i
                    max_jump_pos = pos + i
            
            
            pos = max_jump_pos
            print(pos)
            
        return res