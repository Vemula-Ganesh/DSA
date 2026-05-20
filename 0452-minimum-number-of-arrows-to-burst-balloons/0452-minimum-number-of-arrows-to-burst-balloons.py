class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points.sort()
        # prev=points[0]
        # # count=len(points)
        # count=0
        # for i in points[1:]:
        #     if i[0]<=prev[1]:
        #         count+=1
        #         prev=i
        #     else:
        #         count+=1
        # return count
        n=len(points)
        points.sort(key=lambda x:x[1])
        end=points[0][1]
        arr=0
        left=0
        while left < n :
            end=points[left][1]
            right=left+1
            while right < n and points[right][0]<=end:
                right+=1
            arr += 1
            left=right
        return arr

