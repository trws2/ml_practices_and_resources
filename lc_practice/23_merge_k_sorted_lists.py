# runtime: O(nlog(|lists|))
# space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, id(head), head))

        dummy_head = ListNode()
        cur = dummy_head
        while min_heap:
            min_val, _, node = heapq.heappop(min_heap)
            cur.next = node
            cur = node

            if cur.next:
                heapq.heappush(min_heap, (cur.next.val, id(cur.next), cur.next))

        return dummy_head.next


# linear time solution that runs slow
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur = dummy_head
        
        def get_min(lists: List[Optional[ListNode]]) -> Tuple[Optional[ListNode], List[Optional[ListNode]]]:
            cur_min = float('inf')
            cur_min_node = None

            for h in lists:
                if h is None:
                    continue

                if h.val < cur_min:
                    cur_min_node = h
                    cur_min = h.val

            new_list_heads = []
            if cur_min_node is None:
                new_list_heads = [None] * len(lists)
            else:
                for l in lists:
                    if l == cur_min_node:
                        new_list_heads.append(cur_min_node.next)
                    else:
                        new_list_heads.append(l)

            return cur_min_node, new_list_heads
            
        while True:
            next_node, lists = get_min(lists)
            if next_node is None:
                break
            cur.next = next_node
            cur = next_node
        
        return dummy_head.next
        
