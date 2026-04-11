class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k = k%n
        temp = nums[n-k:n]

        i = n-k-1
        j = n-1

        while i >= 0:

            nums[j] = nums[i]
            i -= 1
            j -= 1
        
        nums[0:k] = temp
    
        return nums
        

        