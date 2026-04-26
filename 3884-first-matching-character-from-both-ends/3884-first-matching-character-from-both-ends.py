class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                return i
            i+=1
            j-=1
        if len(s)%2!=0:
            return len(s)//2
        return -1


