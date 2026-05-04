class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)//2):
            min1=nums.pop(nums.index(min(nums)))
            min2=nums.pop(nums.index(min(nums)))
            result.extend([min2,min1])
        return result
        
            