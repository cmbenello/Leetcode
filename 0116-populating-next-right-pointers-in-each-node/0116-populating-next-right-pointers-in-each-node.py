"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy = root
        
        q1 = deque()
        q2 = deque()
        
        q1.append(root)
        
        while q1:
            length = len(q1)
            
            for i in range(len(q1)):
                curr = q1.popleft()
                
                if len(q1) != 0:
                    nex = q1[0]
                else:
                    nex = None
                if curr:
                    curr.next = nex
                    
                    if curr.left:
                        q2.append(curr.left)
                    if curr.right:
                        q2.append(curr.right)
            
            q1 = q2
            q2 = deque()

        return dummy
        
        