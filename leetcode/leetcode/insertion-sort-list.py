# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        dummy = ListNode(0, head)
        priv, curr = head, head.next

        while curr:
            if priv.val <= curr.val:
                priv, curr = curr, curr.next
            else:
                to_find = dummy
                while to_find.next.val <= curr.val:
                    to_find = to_find.next

                temp = curr.next
                curr.next = to_find.next
                to_find.next = curr
                priv.next = temp
                curr = temp
                
        return dummy.next