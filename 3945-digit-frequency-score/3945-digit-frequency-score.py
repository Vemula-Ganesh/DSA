class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=0
        n=str(n)
        for i in set(n):
            result+=int(i)*n.count(i)
        return result

            


        