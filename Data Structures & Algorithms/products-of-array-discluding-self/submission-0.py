class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prepro = [1]*(n+1)
        for i in range(1,n+1):
            prepro[i] = prepro[i-1]*nums[i-1]

        sufpro = [1]*(n+1)
        for i in range(n-1,-1,-1):
            sufpro[i] = sufpro[i+1]*nums[i]

        res = []

        for i in range(n):
            pro = prepro[i]*sufpro[i+1]
            res.append(pro)
        return res

