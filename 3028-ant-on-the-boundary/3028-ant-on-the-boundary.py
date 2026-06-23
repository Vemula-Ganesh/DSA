class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count=0
        no_steps=0
        for i in nums:
            no_steps+=i
            if no_steps==0:
                count+=1
        return count