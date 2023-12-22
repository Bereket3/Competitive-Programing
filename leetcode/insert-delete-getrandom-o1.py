class RandomizedSet:

    def __init__(self):
       self.cont = {}
       self.data = []

    def insert(self, val: int) -> bool:
        if self.cont.get(val, -1) == -1:
            self.data.append(val)
            self.cont[val] = len(self.data)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        index = self.cont.get(val, -1)
        
        if index>-1:
            temp = self.data[-1]
            self.data[index] = temp
            self.cont[temp] = index
            del self.cont[val]
            self.data.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)
