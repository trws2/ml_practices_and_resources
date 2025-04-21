# runtime: O(n + m)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        dummy = ListNode()
        cur = dummy

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    cur = list1
                    list1 = list1.next
                    continue
                else:
                    cur.next = list2
                    cur = list2                    
                    list2 = list2.next
                    continue

            if list1:
                cur.next = list1
                cur = list1
                list1 = list1.next                
                continue
            
            if list2:
                cur.next = list2
                cur = list2                    
                list2 = list2.next
                continue
        
        return dummy.next

