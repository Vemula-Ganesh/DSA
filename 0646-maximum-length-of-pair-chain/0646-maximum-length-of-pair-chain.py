class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # n=len(pairs)
        # pairs.sort()
        # dp=[1]*n
        # for i in range(1,n):
        #     for j in range(i):
        #         if pairs[j][1]<pairs[i][0]:
        #             dp[i]=max(dp[i],dp[j]+1)
        # return max(dp)

#=========================================================================

        pairs.sort(key=lambda x:x[1])
        prev=pairs[0]
        count=1
        for i in pairs[1:]:
            if i[0]>prev[1]:
                count+=1
                prev=i
        return count
        pairs.sort(key=lambda x: x[1])