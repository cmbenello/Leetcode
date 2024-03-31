class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for i in range(len(grid[0]))] for i in range(len(grid))]
        
        
        # dp[i][j] = grid[i][j] + min(dp[i + 1 ][j], dp[i][j + 1])
        
        
        def dynamic(i, j) -> int:
            if j == len(grid[0]) - 1 and i == len(grid) - 1:
                dp[i][j] = grid[i][j]
                return grid[i][j]
            
            
            val1 = float('inf')
            val2 = float('inf')
            
            if j < len(grid[0]) - 1:
                if dp[i][j + 1] == float('inf'):
                    dp[i][j + 1] = dynamic(i, j + 1)
                val1 = dp[i][j + 1]
            
            if i < len(grid) - 1:
                if dp[i + 1][j] == float('inf'):
                    dp[i + 1][j] = dynamic(i + 1, j)
                val2 = dp[i + 1][j]
                
            # print(val1, val2, dp, grid)
            dp[i][j] = grid[i][j] + min(val1, val2)
            return dp[i][j]
            
        res = dynamic(0,0)
        # print(dp)
        return res