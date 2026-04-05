class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()

        for num in nums:
            ans.add(num)

        
        if len(ans) == len(nums):
            return False
        
        return True