class Solution(object):
    def leftRightDifference(self, nums):
        la=[0]
        ra=[]
        for i in range(1,len(nums)+1):
            ra.append(sum(nums[i:]))
            la.append(sum(nums[:i]))
        ra.append(0)
        for i in range(len(nums)):
            nums[i]=abs(la[i]-ra[i])
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        