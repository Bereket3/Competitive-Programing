# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        my_counter = Counter()
        while head:
            my_counter[head.val] += 1
            head = head.next

        my_list = [*my_counter.keys()]
        
        new = []

        for i in my_list[::-1]:
            new +=[ListNode(i, None)]

        for i in range(1, len(new)):
            new[i].next = new[i-1]

        return new[-1]

