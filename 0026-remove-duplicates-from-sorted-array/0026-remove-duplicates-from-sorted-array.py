class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        prev = nums[0]
        jump = 0
        for i in range(1, len(nums)):
            if prev == nums[i]:
                jump += 1
                k -= 1
            
            nums[i - jump] = nums[i]
            prev = nums[i - jump]
            k += 1
        
        print(k)
        return k
            
                