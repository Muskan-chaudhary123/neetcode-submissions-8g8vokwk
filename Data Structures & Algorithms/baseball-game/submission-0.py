class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                res = stack[len(stack)-1] + stack[len(stack)-2]
                stack.append(res)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                res = stack[len(stack)-1] * 2
                stack.append(res)
            
            else:
                stack.append(int(op))
        
        return sum(stack)