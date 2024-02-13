# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        
        x_min = y_min = -1
        x_max, y_max =n, m
        dx, dy = 1, 0
        posx = posy = 0
        
        for _ in range(x_max*y_max):
            if not head:
                break
            if posx < x_max and posx > x_min and posy < y_max and posy > y_min:
                matrix[posy][posx] = head.val
                head = head.next
                posx += dx
                posy += dy
            else:
                if dx == 1 and dy == 0:
                    dx = 0
                    dy = 1
                    posx -= 1
                    posy += 1
                    matrix[posy][posx] = head.val
                    head = head.next
                    posx += dx
                    posy += dy
                    y_min += 1
                elif dx == 0 and dy == 1:
                    dx = -1
                    dy = 0
                    posx -= 1
                    posy -= 1
                    matrix[posy][posx] = head.val
                    head = head.next
                    posx += dx
                    posy += dy
                    x_max -= 1
                elif dx == -1 and dy == 0:
                    dx = 0
                    dy = -1
                    posx += 1
                    posy -= 1
                    matrix[posy][posx] = head.val
                    head = head.next
                    posx += dx
                    posy += dy
                    y_max -= 1
                else:
                    dx = 1
                    dy = 0
                    posx += 1
                    posy += 1
                    matrix[posy][posx] = head.val
                    head = head.next
                    posx += dx
                    posy += dy
                    x_min += 1
        
        return matrix