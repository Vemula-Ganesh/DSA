class Solution:
    def countAsterisks(self, s: str) -> int:
        f=1
        result=0
        # stack=[]
        for word in s:
            if word=="|" and f==0:
                f=1
            elif word=="|":
                f=0
            elif word=="*" and f:
                result+=1
        return result
                
            # if word=="|":
                # stack.append([])
            # if stack:
            #     stack.pop()
        #     elif word=="*" and not stack:
        #         result+=1
        # return result
                