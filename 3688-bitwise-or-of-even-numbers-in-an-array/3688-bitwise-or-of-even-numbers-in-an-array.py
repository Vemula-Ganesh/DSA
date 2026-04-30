class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        f=0
        result=0
        for i in nums[::]:
            if i%2==0:
                f=1

                print(i)
                result |=i
        if f:
            return result
        return 0

        