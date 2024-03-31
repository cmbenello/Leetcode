class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #option 1: go through all the substrings and keep track of the longest found that doesn't contain any repeating characters, will have 0(n^2)
    
        if len(s) <= 1:
            return len(s)
        
        count = [0] * 128
        
        res = 0

        i, j = 0, 0
        
        while j < len(s):
            while count[ord(s[j])] > 0: 
                count[ord(s[i])] -= 1
                i += 1

            count[ord(s[j])] += 1
            res = max(res, j - i + 1)
            j += 1
            
        return res