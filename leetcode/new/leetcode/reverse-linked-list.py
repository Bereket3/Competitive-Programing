# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _reversed = None
        while head != None:
            nxt = head.next
            head.next = _reversed
            _reversed = head
            head = nxt

        return _reversed