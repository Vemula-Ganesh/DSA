class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # aresult=[]
        # for i in nums:
        #     a=i
        #     result=[]
        #     while a:
        #         result.insert(0,a%10)
        #         a=a/10
        #         # print(a%10)
        #     aresult.extend(result)
        # return aresult

        result=[]
        for i in nums[::-1]:
            digit=i
            # result=[]
            while digit:
                result.insert(0,digit%10)
                digit=digit/10
                # print(a%10)
        return result
                