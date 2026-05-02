class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result=0
        k=3
        for i in range(len(s)-k+1):
                if s[i:k+i][0]!=s[i:k+i][1] and s[i:k+i][1]!=s[i:k+i][2] and s[i:k+i][0]!=s[i:k+i][2]:
                    result+=1
        return result