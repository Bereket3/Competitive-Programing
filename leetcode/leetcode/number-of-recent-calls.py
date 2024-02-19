from collections import deque 

class RecentCounter:

    def __init__(self):
        self.qu = deque()
        

    def ping(self, t: int) -> int:
        while self.qu and t - self.qu[0] > 3000:
            self.qu.popleft()
        self.qu.append(t)
        return self.qu.__len__()

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)