import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        heap = []

        for key in freq:

            heapq.heappush(heap,(freq[key] , key))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        
        while heap:

            count , key = heapq.heappop(heap)
            res.append(key)
            
        return res


