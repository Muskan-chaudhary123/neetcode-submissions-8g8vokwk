class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for  brc in s:
            
            if brc == '[' or brc == '{' or brc == '(':
                stack.append(brc)
            else:
                if not stack:
                    return False
                else:
                    if self.validate(brc,stack):
                        stack.pop()
                    else:
                        return False

        if len(stack) == 0:
            return True
        return False        
    
    def validate(self,brc,stack):
        if brc == ']' and stack[-1] == '[':

            return True
        if brc == '}' and stack[-1] == '{':
            
            return True

        if brc == ')' and stack[-1] == '(':
            
            return True
        return False