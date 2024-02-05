class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        prev = nums[0]
        counter = 1
        jump = 0
        for i in range(1, len(nums)):
            if prev == nums[i]:
                if counter < 2:
                    counter += 1
                else:
                    jump += 1
                    k -= 1
            else:
                counter = 1
            nums[i - jump] = nums[i]
            prev = nums[i - jump]
            k += 1
        
        return k

        