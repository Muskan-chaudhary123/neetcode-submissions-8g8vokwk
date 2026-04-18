class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split('/')

        stack = []
        
        for d in directory:
            if d == "" or d =='.':
                continue
            elif d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        return '/' + '/'.join(stack)
            

