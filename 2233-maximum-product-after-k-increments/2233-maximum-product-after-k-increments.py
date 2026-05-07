import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            heapq.heappush(nums,heapq.heappop(nums)+1)
        prod=1
        for i in nums:
            prod=(prod*i)%(10**9+7)
        return prod
        