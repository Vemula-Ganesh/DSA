class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # result=""
        uc=0
        for i in arr:
            if arr.count(i)==1:
                uc+=1
                if uc==k:
                    return i
        return ""

        