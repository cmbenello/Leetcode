# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        dummy = ListNode()
        dummy.next = head
        
        fast = dummy.next
        slower = dummy
        slow = slower.next
        
        
        while fast and fast.next:
            fast = fast.next.next
            slower = slow
            slow = slow.next
        
        mid = slow
        
        slower.next = None
        
        res = TreeNode()
        res.val = mid.val
        res.left = self.sortedListToBST(dummy.next)
        res.right = self.sortedListToBST(mid.next)
        
        return res