class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum=nums[0]
        minsum=nums[0]
        totalsum=nums[0]
        curmaxsum=nums[0]
        curminsum=nums[0]
        for i in range(1,len(nums)):
            totalsum+=nums[i]
            curmaxsum=max(curmaxsum+nums[i],nums[i])
            maxsum=max(curmaxsum,maxsum)
            curminsum=min(curminsum+nums[i],nums[i])
            minsum=min(curminsum,minsum)
        cirsum=totalsum-minsum
        if cirsum==0:
            return maxsum
        return max(maxsum,cirsum)
        return maxsum if totalsum==minsum else max(maxsum,totalsum-minsum)
