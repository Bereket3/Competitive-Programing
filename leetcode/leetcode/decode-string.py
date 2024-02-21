class Solution:
    def decodeString(self, s: str) -> str:
        __the_stack: list = []
        __the_number: int = 0
        __the_string: str = ''

        for i in s:
            if i == '[':
                __the_stack.append(__the_string)
                __the_stack.append(__the_number)
                __the_string = ''
                __the_number = 0
            elif i == ']':
                number = __the_stack.pop()
                priv = __the_stack.pop()
                __the_string = priv + __the_string*number

            elif i.isdigit():
                __the_number = 10*__the_number + int(i)
            else:
                __the_string += i
                
        return __the_string