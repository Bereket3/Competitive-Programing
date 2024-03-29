class BrowserHistory:

    def __init__(self, homepage: str):
        self.tofor = []
        self.tocurr = [homepage]
        

    def visit(self, url: str) -> None:
        self.tofor = []
        self.tocurr += [url]
        

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.tocurr) > 1:
            self.tofor.append(self.tocurr.pop())
            steps -=1
        return self.tocurr[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.tofor) > 0 :
            self.tocurr.append(self.tofor.pop())
            steps -=1
        return self.tocurr[-1]

        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)