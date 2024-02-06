class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for num in nums]

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        backward = 1
        for i in range(len(nums) - 1, - 1, -1):
            res[i] *= backward
            backward *= nums[i]

        return res