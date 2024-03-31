class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # if we reverse if this is the same as trying to find the longest common substring between the two of them
        
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
        
        t = s[::-1]
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]