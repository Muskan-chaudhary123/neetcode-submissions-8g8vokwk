class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        resSet = set()

        for num in nums:
            resSet.add(num)
        
        ans = 0
        for num in resSet:
            if num-1 not in resSet:
                start = num
                count = 1

                while start + 1 in resSet:
                    start += 1
                    count += 1
                
                ans = max(ans,count)
        
        return ans 