class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == '+':
                f_ = s.pop()
                s_ = s.pop()
                s.append(f_ + s_)

            elif i == '/':
                f_ = s.pop()
                s_ = s.pop()
                if s_ * f_ > 0:
                    s.append(math.floor(s_ / f_))
                else:
                    s.append(math.ceil(s_ / f_))

            elif i == '-':
                f_ = s.pop()
                s_ = s.pop()
                s.append(s_ - f_)
            elif i == '*':
                f_ = s.pop()
                s_ = s.pop()
                s.append(f_ * s_)
            else:
                s.append(int(i))
            
        return s.pop()