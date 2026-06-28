class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        # if n%2!=0:
        #     return int(sum(nums1)/n)
        # return sum(nums1)/n
        # if n==1:
        #     return nums1[0]
        if n%2!=0:
            # print(n%2)
            return nums1[n//2]/1
            # return int(sum(nums1)/n)
        # i=0
        # j=n-1
        # while i<j:
        #     i+=1
        #     j-=1
        # print(i)
        # print(j)

        return (nums1[(n//2)-1]+nums1[n//2])/2

