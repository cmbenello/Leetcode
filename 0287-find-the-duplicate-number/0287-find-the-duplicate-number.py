class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            temp = nums[i]
            if temp < 0:
                temp = nums[i] * -1
            
            if nums[temp - 1] < 0:
                return temp
            
            else:
                nums[temp - 1] *= -1
                
                
        return 0