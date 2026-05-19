class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        # freq=counter(groupsize)
        # for i,count in freq.items():
        #     if i%
        # result=[[0]]]
        groups={}
        res=[]
        for i,size in enumerate(groupSizes):
            
            if size not in groups:
                groups[size]=[]
            groups[size].append(i)
            if len(groups[size])==size:
                res.append(groups[size])
                groups[size]=[]
        return res

        
        # for i in groupSizes:
        #     if i not in result[ri]:
        #         result[ri].append(i)
        #         ri+=1
        #     else:
