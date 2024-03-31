class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #option 1: go through all the substrings and keep track of the longest found that doesn't contain any repeating characters, will have 0(n^2)
    
        res = 0
        for start in range(len(s)):
            seen = set()
            i = start
            while i < len(s):
                if s[i] in seen:
                    break
                    
                if s[i] not in seen:
                    seen.add(s[i])
                    i += 1
            res = max(res, len(seen))
            
        
        return res