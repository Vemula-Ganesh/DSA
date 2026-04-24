class Solution:
    def countPoints(self, rings: str) -> int:
        result=0
        for i in range(9+1):
            B="B"+str(i)
            G="G"+str(i)
            R="R"+str(i)
            if B in rings and G in rings and R in rings:
                result+=1
        return result