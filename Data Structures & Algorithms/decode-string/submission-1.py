class Solution:
    def decodeString(self, s: str) -> str:
        curr_str = ''
        curr_num = 0
        stack_num = []
        stack_str = []

        for ch in s:
            if ch == '[':
                stack_num.append(curr_num)
                stack_str.append(curr_str)
                curr_str = ''
                curr_num = 0
            elif ch.isalpha():
                curr_str += ch
            
            elif ch == ']':
                prev_num = stack_num.pop()
                prev_str = stack_str.pop()
                curr_str = prev_str + curr_str*prev_num
            else:
                curr_num = curr_num * 10 + int(ch)
        
        return curr_str
