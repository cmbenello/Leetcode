class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0 for i in range(len1 + 1) ] for j in range(len2 + 1)]
        
        
        
            
        # abcdefg acefg
        # abcde + fg ace + fg
        # lcs(abcde, ace) = lcs(abcd, ac) + 1 if text[i] == text2[j] else
        
        
        for col in reversed(range(len1)):
            for row in reversed(range(len2)):
                if text1[col]  == text2[row]:       
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        
        return dp[0][0]
            