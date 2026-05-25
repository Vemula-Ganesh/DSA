class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # pr=""
        # mi=0
        # for i in strs:
        #     mi=min(len(i),mi)
        # # for i in range(m):
        # #     if strs[0][:i]==strs[-1][:i]:
        # #         pr=strs[0][:i]
        # # for i in strs:
        # #     if pr not in i :
        # #         return pr
        # #     return pr
        # for i in range(mi):
        #     if 


        # mls=0
        # ls=0
        # for i in s:
        #     ls=len(s)
        #     if mls>ls:
        #         mls=ls
        # for i in strs:
        #     for j in i:
        #         for i in range(mls):
                    
        # for i in strs:
        #     for j in 























        r=1
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                # if strs[j].startswith(s[:i+1]):
                r&=strs[j].startswith(strs[0][:i+1])
                if not r:
                    return strs[0][:i]
        if r:
            return strs[0]
        return ""