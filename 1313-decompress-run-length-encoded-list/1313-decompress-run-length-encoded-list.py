class Solution(object):
    def decompressRLElist(self, nums):
        result=[]
        for i in range(0,len(nums),2):
            result.extend([nums[i+1]]*nums[i]) 
            # result.append(nums[i]*
        return result

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        