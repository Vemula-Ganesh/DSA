class Solution:
    def sortSentence(self, s: str) -> str:
        # ns=""
        # l=[]
        # for i in range(s.count(" ")+2):l.append(" ")
        # w=""
        # for i in s[:]:
        #     if i!=" ":
        #         w+=i
        #     else:
        #         # l[w[-1]-1]
        #         l[int(w[-1])-1]=w
        #         w=""
        # for i in l:
        #     ns+=i[:len(i)-1]+" "
        # return ns
        s=s.split()
        s.sort(key=lambda x:x[-1])
        result=""
        for i in s:
            result+=" "+i[:-1]
        return result.strip()
            