class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = list(s)

        st = ""

        for l in ls:
            if l.isalnum():
                st += l.lower()
        i = 0 
        j = len(st)-1
        while i < j:
            if st[i] != st[j]:
                return False
            
            i += 1
            j -= 1
        
        return True

