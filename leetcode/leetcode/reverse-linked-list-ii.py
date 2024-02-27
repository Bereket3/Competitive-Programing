# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or right == left: return head
        dummy = ListNode('dummy', head)
        pr = dummy
        for i in range(left - 1):
            pr = pr.next

        p, q = pr, pr.next
        curr = q
        
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = pr
            pr, curr = curr, nxt
        

        p.next = pr
        q.next = curr
        return dummy.next