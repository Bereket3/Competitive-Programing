class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        mod = 10 ** 9 + 7
        n = len(arr)
        left, right = [0]*n, [0]*n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        
        return sum(n * l * r for n, l, r in zip(arr, left, right)) %  mod
