class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        result=0
        nums=[str(i) for i in nums]
        for i in nums:
            result+=i.count(str(digit))
        return result