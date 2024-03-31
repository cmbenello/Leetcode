class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Go through using a sliding window, keep track of the characters that you have passed and their quantity using a hashmap
        # while the sum of of "others" is less than k keep going 
        

        
        count = {}        
        maxf = 0
        l = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            
            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1 
            res = max(res, r - l + 1)
        return res