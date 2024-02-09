class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        
        left = right = 0
        
        longest = 0
        
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
            
            longest = max(longest, right -left + 1)
            
            right += 1
                
        return longest