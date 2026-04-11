class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n):

                if j > i+1  and nums[j] == nums[j-1]:
                    continue
                
                low = j+1
                high = n -1

                while low < high:
                    tar = nums[i] + nums[j] + nums[low] + nums[high]

                    if tar == target:
                        res.append([nums[i] , nums[j] , nums[low] , nums[high]])
                        low += 1
                        high -= 1

                        while low < high  and nums[high] == nums[high+1]:
                            high -= 1
                        while low < high and nums[low] == nums[low -1]:
                            low += 1
                    
                    elif tar > target:
                        high -= 1
                    
                    else:
                        low += 1
        return res