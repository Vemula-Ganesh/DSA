class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        result=[0]*n
        for i ,t in enumerate(temperatures):
            while (stack and t>stack[-1][0]):
                temp,ind=stack.pop()
                result[ind]=i-ind
            stack.append([t,i])
        return result
        # for i in range(n):
        #     if not stack:
        #         stackk.append(temparature[i])
        #     else:
        #         if temperatures[-1]>temparature
