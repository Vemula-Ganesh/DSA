class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smin=arrays[0][0]
        smax=arrays[0][-1]
        diff=0
        for i in range(1,len(arrays)):
            curmin=arrays[i][0]
            curmax=arrays[i][-1]

            diff=max(diff,curmax-smin)
            diff=max(diff,smax-curmin)

            smin=min(smin,curmin)
            smax=max(smax,curmax)
        return diff