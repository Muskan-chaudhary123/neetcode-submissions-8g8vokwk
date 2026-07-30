class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for num in freq:
            if freq[num] > 1:
                return True
        return False