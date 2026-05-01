class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # for i in t :
        #     if i not in s:
        #         return i
        # for i in range(len(s)):
        #         # print(t.replace(i,""))
        #         t=t.replace(s[i],"",i+1)
        # return t
        # while i in 




        
        # s=list(s)
        # t=list(t)
        # def sorted(s):
        #     for i in range(len(s)-1):
        #         temp=s[i]
        #         for j in range(i+1,len(s)):
        #             if s[i]>s[j]:
        #                 temp=s[j]
        #             s[i]=temp
        #             s[j]=s[i]
        #     return s
        s=sorted(s)
        s.append(" ")
        print(s)
        t=sorted(t)
        print(t)
        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i]