class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lis = deque()
        i = 0
        j = 0
        ans = []
        while j < len(nums):

            while lis and lis[-1] < nums[j]:
                lis.pop()
            lis.append(nums[j])

            if j-i+1 < k:
                j += 1
            
            else:
                ans.append(lis[0])
                if nums[i] == lis[0]:
                    lis.popleft()
                i += 1
                j += 1
        
        return ans
