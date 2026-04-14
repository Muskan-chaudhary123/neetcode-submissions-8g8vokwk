class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        res = 0
        ans = float('inf')

        while j < len(nums):
            res += nums[j]

            while res >= target:
                ans = min(ans,j-i+1)
                res -= nums[i]
                i += 1
            
            j += 1
        
        if ans == float('inf'):
            return 0
        
        return ans
