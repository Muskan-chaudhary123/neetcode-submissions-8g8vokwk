class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_hash = {}

        for i in range(len(s1)):
            if s1[i] in s1_hash:
                s1_hash[s1[i]] += 1
            else:
                s1_hash[s1[i]] = 1
        
        window = len(s1)
        s2_hash = {}
        i = 0
        j = 0
        while j < len(s2):
            if s2[j] in s2_hash:
                s2_hash[s2[j]] += 1
            else:
                s2_hash[s2[j]] = 1
            
            if j - i + 1 == window:
                if s1_hash == s2_hash :
                    return True
                
                s2_hash[s2[i]]  -= 1
                if s2_hash[s2[i]] == 0:
                    del s2_hash[s2[i]] 
                i += 1
                
            j += 1
        return False

