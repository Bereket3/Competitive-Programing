class MyLinkedList:
    class Node:
        def __init__(self, val, next = None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        temp = self.head
        indx = 0
        while temp:
            if indx == index:
                return temp.val
            indx += 1
            temp = temp.next
    
        return -1


    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = self.Node(val)

        else:
            new_head = self.Node(val)
            old_head = self.head
            new_head.next = old_head
            self.head = new_head
        self.len += 1


    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = self.Node(val)
            self.len += 1
            return 
        new = self.head
        while new.next:
            new = new.next
        new.next = self.Node(val)
        self.len += 1
    

    def __len__(self):
        return self.len


    def addAtIndex(self, index: int, val: int) -> None:
        new = self.Node(val)
        if index == 0:
            return self.addAtHead(val)
        elif index == len(self):
            return self.addAtTail(val)
        elif index > len(self):
            return 
        else:
            temp = self.head
            count = 0
            while temp:
                if count == index - 1:
                    new.next = temp.next
                    temp.next = new
                    break
                count += 1
                temp = temp.next
            self.len += 1


    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        indx = 0
        current = self.head
        while current.next and indx < index:
            previous = current
            current = current.next
            indx += 1
        if indx < index:
            return 
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
        self.len -= 1
    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)