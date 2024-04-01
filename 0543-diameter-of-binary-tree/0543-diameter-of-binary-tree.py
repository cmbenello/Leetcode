# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diamatre of binary tree is going to be max(depth l + dpeth r, diamater of l , diamater of r)
        if root is None:
            return 0
        def depth(root):
            if root is None:
                return 0
            
            return 1 + max(depth(root.left), depth(root.right))
        
        
        res = depth(root.left) + depth(root.right) 
        
        return max(res, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)) 