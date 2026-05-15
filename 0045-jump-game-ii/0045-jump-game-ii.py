class Solution:
    def jump(self, nums: List[int]) -> int:
        # jump=currend=fast=0
        # for i in range(len(nums)-1):
        #     fast=max(fast,i+nums[i])
        #     if i==currend:
        #         jump+=1
        #         currend=fast
        # return jump
        n=len(nums)
        dp=[float("inf")] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1,nums[i]+1):
                if i+j<n:
                    # d[j]=min(d(j),d[i]+1)
                    dp[i+j]=min(dp[i+j],dp[i]+1)
        return  dp[-1]
            