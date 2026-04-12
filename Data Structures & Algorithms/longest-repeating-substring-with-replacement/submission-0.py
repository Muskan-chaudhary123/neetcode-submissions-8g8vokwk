class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        i = 0
        j = 0
        ans = 0
        max_freq = 0
        
        while j < len(s):
            if s[j] in char:
                char[s[j]] += 1
            else:
                char[s[j]] = 1
            max_freq = max(max_freq, char[s[j]])


            if j -i + 1 - max_freq > k:
                while j - i + 1 - max_freq > k:

                    char[s[i]] -= 1
                    i += 1
            ans = max(ans , j-i+1)
            j += 1
        
        return ans 


