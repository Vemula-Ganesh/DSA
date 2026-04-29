class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            c_nums=nums.copy()
            c_nums.pop(i)
            if c_nums==sorted(list(set(c_nums))):
                    return True
        return False