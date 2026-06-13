class Solution:
    def replaceDigits(self, s: str) -> str:
        result=s[0]
        for i in range(1,len(s)):
            if s[i].isdigit():
                result+=chr(ord(s[i-1])+int(s[i]))
            else:
                result+=s[i]
        return result