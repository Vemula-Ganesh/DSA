class Solution:
    def minLength(self, s: str) -> int:

        # s=s.replace("AB","")
        # s=s.replace("CD","")
        # print(s.replace("AB",""))
        # # print(s.replace("CD",""))
        while "AB" in s or "CD" in s:
            if "AB" in s:s=s.replace("AB","")
            elif "CD" in s:s=s.replace("CD","")
        return len(s)