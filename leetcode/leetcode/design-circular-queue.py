class Node:
    def __init__(self, val='dummy',next = None):
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.queue = Node()
        self.last = 0

    def __repr__(self):
        arr = []
        copy = self.queue
        while copy:
            arr.append(copy.val)
            copy = copy.next
        return str(arr)

    def enQueue(self, value: int) -> bool:
        if self.size < self.max_size:
            new_node = Node(value)
            copy = self.queue
            while copy and copy.next:
                copy = copy.next
            
            copy.next = new_node
            self.last = value
            self.size += 1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.queue.next = self.queue.next.next
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.size == 0: return -1
        return self.queue.next.val

    def Rear(self) -> int:
        if self.size == 0: return -1
        return self.last

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.max_size else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()