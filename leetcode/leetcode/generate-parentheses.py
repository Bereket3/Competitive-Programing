class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final_list=[]

        def backtrack(i, j, stack):
            if i==j==n:
                final_list.append("".join(stack))
                return

            if i<n:
                stack.append('(')
                backtrack(i+1, j, stack)
                stack.pop()

            if j<n and i>j:
                stack.append(')')
                backtrack(i, j+1, stack)
                stack.pop()
                
        backtrack(0,0, [])
        return final_list

        