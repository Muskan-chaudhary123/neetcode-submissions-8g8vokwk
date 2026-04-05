class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        maj = nums[0]

        for num in nums:
            if vote == 0:
                vote += 1
                maj = num
            
            if num == maj:
                vote += 1
            else:
                vote -= 1
        
        return maj