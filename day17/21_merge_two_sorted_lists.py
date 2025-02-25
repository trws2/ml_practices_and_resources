# Runtime: O(n)
# space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2

        if not list2:
            return list1

        # create a dummy node
        dummy = ListNode(0)
        cur = dummy
        l1 = list1
        l2 = list2

        # while both l1 and l2 are not None
        # if l1.val < l2.val, assign current node to l1 and move l1 to l1.next
        # else, assign current node to l2 and move l2 to l2.next

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

        return dummy.next

