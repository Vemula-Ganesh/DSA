class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        #     print(type(nums[i]))
            nums[i]=sum(list(map(int,nums[i])))
        # print(nums)
        return min(nums)

        n="12"
        print(list((map(int,n))))