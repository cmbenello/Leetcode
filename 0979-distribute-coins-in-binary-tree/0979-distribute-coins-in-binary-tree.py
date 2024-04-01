# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        
        #Count the number of coins in each tree and sub tree versus the number of nodes return the differnce
        # Ie returning 5 means that there are 5 extra coins that there are suppposed to be and -5 means 5 nodes are missing coins
        self.ans = 0
        def dfs(node):
            if node is None:
                return 0
            self.ans += abs(dfs(node.left)) + abs(dfs(node.right))
            
            return node.val - 1 + dfs(node.left) + dfs(node.right)
        
        
        dfs(root)
        return self.ans