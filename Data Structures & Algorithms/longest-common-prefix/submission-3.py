class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])

        res = ""

        for i in range(n):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return res
            
            res += strs[0][i]
        
        return res