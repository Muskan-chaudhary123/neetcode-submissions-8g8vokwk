class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}

        for ch in t:
            if ch in hash_t:
                hash_t[ch] += 1
            else:
                hash_t[ch] = 1
        
        res = float('inf')
        start = 0
        req = len(hash_t)
        i = 0
        j = 0
        while j<len(s):
            if s[j] in hash_t:
                hash_t[s[j]] -= 1
                if hash_t[s[j]] == 0:
                    req -= 1
            
            while req == 0:
                if j - i + 1 < res:
                    res = j-i+1
                    start = i
                if s[i] in hash_t:
                    hash_t[s[i]] += 1
                    if hash_t[s[i]] > 0:
                        req += 1
                i += 1
            j += 1
        
        if res == float('inf'):
            return ""
        
        return s[start:start+res]
        

                


