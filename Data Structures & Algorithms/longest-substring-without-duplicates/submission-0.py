class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        unique = set()
        i = 0
        j = 0
        while j < len(s):
            if s[j] in unique:
                while s[j] in unique:
                    unique.remove(s[i])
                    i += 1
            unique.add(s[j])

            ans = max(ans,j-i+1)
            j += 1
        return ans  