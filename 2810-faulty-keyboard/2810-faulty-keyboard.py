class Solution:
    def finalString(self, s: str) -> str:
        ns=""
        # ci=s.count("i")
        for i in range(len(s)):
            if s[i]=="i":
                print(s[i-1::-1])
                s=s[i-1::-1]+" "+s[i+1:]
                print(s)
                # pi=i
        return s.replace(" ","")
