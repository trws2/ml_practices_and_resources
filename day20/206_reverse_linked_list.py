# runtime: O(n)
# storage: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prepare a dummy node at the beginnnig as previous node, it then 
        # traverse each node and reverse the next to make it point to prev
        if head is None:
            return None

        dummy = ListNode(-1, next=None)
        prev = dummy
        node = head
        while node is not None:
            ori_next = node.next
            if prev == dummy:
                node.next = None
            else:
                node.next = prev
            prev = node
            node = ori_next
        
        return prev

