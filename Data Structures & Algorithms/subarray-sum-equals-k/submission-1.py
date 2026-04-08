from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prehash = defaultdict(int)
        presum = 0
        count = 0

        for num in nums:
            presum += num
            if presum == k:
                count += 1
            
            if presum - k in prehash:
                count += prehash[presum - k]
            
            prehash[presum] += 1
        
        return count

