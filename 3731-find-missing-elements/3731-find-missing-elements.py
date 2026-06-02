class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        Min=min(nums)
        Max=max(nums)
        result=[]
        for i in range(Min,Max):
            if i not in nums:
                result.append(i)
        return result