# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        
        q1 = [root]
        q2 = []
        
        while q1:
            length = len(q1)
            for i in range(length):
                
                curr = q1.pop(0)
                
                q1.append(curr.val)
                
                if curr.left:
                    q2.append(curr.left)
                if curr.right:
                    q2.append(curr.right)
                
            res.append(q1)
            q1 = q2
            q2 = []
        
        return res
        