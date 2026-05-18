class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # count=0
        # prevmax=0
        # for index,j in enumerate(arr):
        #     prevmax=max(prevmax,j)

        #     if prevmax==index:
        #         count+=1
        # return count
        st=[]
        for x in arr:
            mx=x
            while st and st[-1]>x:
                mx=max(mx,st.pop())
            st.append(mx)
        return len(st)