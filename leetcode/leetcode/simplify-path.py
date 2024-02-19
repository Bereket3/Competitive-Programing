class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split("/")
        for i in lst:
            if i=="" or i=="." :
                continue
            elif i=="..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        return "/"+"/".join(stack)