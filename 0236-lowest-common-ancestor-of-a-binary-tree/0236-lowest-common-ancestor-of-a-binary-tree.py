# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Find which subtree the nodes are in
        # if they are in the same one then recurisvely call on the subtree
        
        # how to handle the edge case wher the node is the value  - just return the value 
        
        #Helper to check if a node is in the tree
        def get_path(root, curr_path, node):
            if root is None:
                return []
            
            curr_path.append(root)
            
            if root == node:
                return curr_path
            
            path1 = get_path(root.left, curr_path[:], node)
            path2 = get_path(root.right, curr_path[:], node)    
            
            if path1:
                return path1
            else:
                return path2
            
    
        path1 = get_path(root, [], p)
        path2 = get_path(root, [], q)
        
        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            # print(i, path1[i], path2[i])
            i += 1
        
        return path1[i - 1]