class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        d = {}
        for val in nums:
            d[val] = 1
        
        start_items = []
        for key, val in d.items():
            if key - 1 not in d:
                start_items.append(key)
        
        max_len = 1
        for key in start_items:
            curr_len = 1
            curr = key + 1
            while curr in d:
                curr_len += 1
                curr += 1
            if curr_len > max_len:
                max_len = curr_len
        
        return max_len