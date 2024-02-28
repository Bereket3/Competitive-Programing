# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        p = head

        while p:
            p = p.next
            n += 1
        
        tot_element = n // k
        extra = n % k
        out = [None]*k
        curr = head

        for i in range(k):
            temp = curr
            elements = tot_element + (i < extra)
            for j in range(elements - 1):
                if curr:
                    curr = curr.next

            if curr:
                a = curr.next
                curr.next = None
                curr = a

            out[i] = temp

        return out