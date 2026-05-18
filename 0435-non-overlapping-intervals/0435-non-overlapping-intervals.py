class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        result=0
        intervals.sort(key=lambda x : x[1])
        for i in range(1,len(intervals)):
            if intervals [i][0] <intervals[i-1][1]:
                intervals[i]=intervals[i-1]
                result+=1
        return result