# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        res = 0
        while head:
            res = 2*res + head.val
            count += 1
            head = head.next
        return res
        