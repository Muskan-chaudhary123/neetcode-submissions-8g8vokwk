class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = [0]*26

        t_freq = [0]*26

        n = len(s)

        for i in range(n):
            s_freq[ord(s[i]) - ord('a')] += 1
            t_freq[ord(t[i]) - ord('a')] += 1

        if s_freq == t_freq:
            return True
        return False