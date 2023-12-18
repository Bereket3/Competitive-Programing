class FrequencyTracker:
    def __init__(self):
        self.container = Counter()
        self.frequency = Counter()

    def add(self, number: int) -> None:
        self.frequency[number] += 1
        self.container[self.frequency[number]] += 1
        self.container[self.frequency[number] - 1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.frequency[number]:
            self.frequency[number] -= 1
            if self.frequency[number] == 0: 
                del self.frequency[number]
            self.container[self.frequency[number]] += 1
            self.container[self.frequency[number] + 1] -= 1 


    def hasFrequency(self, frequency: int) -> bool:
        return self.container[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)