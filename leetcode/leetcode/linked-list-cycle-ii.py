# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        if not head: return

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                ans = head
                while ans != slow:
                    ans = ans.next
                    slow = slow.next
                return ans

        return 
