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
            # print(q1)
            for val in q1:
                if val.left:
                    q2.append(val.left)
                if val.right:
                    q2.append(val.right)
            
            if q1:
                res.append([i.val for i in q1])
            
            q1 = q2
            q2 = []
        
        return res