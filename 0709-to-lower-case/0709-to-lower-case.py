class Solution:
    def toLowerCase(self, s: str) -> str:

        result=""
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                result+=chr(ord(i)+32)
            else:
                result+=i
        return result
