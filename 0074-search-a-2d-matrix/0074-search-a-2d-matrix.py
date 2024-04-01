class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bounds = []
        
        for i in range(len(matrix)):
            bounds.append(matrix[i][0])
        
        # Do binary serach on the bounds to find the best ones
        
        
        l, r = 0, len(bounds) - 1
        
        while l <= r:
            m = (l + r) // 2
            if bounds[m] > target:
                r = m - 1
            elif bounds[m] < target:
                l = m + 1
            else:
                break
        
        # print(l, r, m)
        # if not l <= r:
        #     return False
        m = (l + r)//2
        # print(m)
        nums = matrix[m]
        l, r = 0, len(nums) - 1 
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            if nums[m] < target:
                l = m + 1
            if nums[m] == target:
                return True
            
        return False