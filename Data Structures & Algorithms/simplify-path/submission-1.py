class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split('/')

        stack = []
        
        for d in directory:
            if d == '..':
                if stack:
                    stack.pop()
            elif d != "" and d !='.':
                stack.append(d)
        
        return '/' + '/'.join(stack)
            

