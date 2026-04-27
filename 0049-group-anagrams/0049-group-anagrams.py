class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort=set([str(sorted(i)) for i in strs])
        # sort=set(sort)
        d={}
        for i in sort:
            d[i]=[]
        for i in strs:
            d[str(sorted(i))].append(i)
        # print(*d.values())
        return [*d.values()]