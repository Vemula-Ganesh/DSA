class Solution(object):
    def largestNumber(self, nums):
        # d
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=list(map(str,nums))
        nums.sort(key=lambda x:x*10,reverse=True)
        res="".join(nums)
        return "0" if res[0]=="0" else res