# runtime: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (not head) or (not head.next):
            return False

        if head.next == head:
            return True

        slow = head.next
        fast = head.next.next

        while slow != fast:
            slow = slow.next

            if fast is None or fast.next is None:
                return False

            fast = fast.next.next
            
        return True            

