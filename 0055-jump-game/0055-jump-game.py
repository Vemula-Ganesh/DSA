class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #    if nums[i]-len(nums[i+1:])==0:
        #     return True
        # return False
        target=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=target:
                target=i
        return target==0
