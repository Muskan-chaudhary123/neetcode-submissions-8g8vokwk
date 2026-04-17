class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(len(temperatures)-1,-1,-1):
            if len(stack) == 0:
                res.append(0)
            
            else:
                if stack[-1][0] > temperatures[i]:
                    res.append(stack[-1][1] - i)
                
                else:
                    while stack and stack[-1][0] <= temperatures[i]:
                        stack.pop()
                    if len(stack) == 0:
                        res.append(0)
                    else:
                        res.append(stack[-1][1] - i)
            stack.append([temperatures[i],i])
        
        return res[::-1]