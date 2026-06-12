class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # result={}
        # for i in range(len(names)):
        #     result[names[i]]=heights[i]
        # print(result.items())
        # result_items=list(result.items())
        # result_items.sort(key=lambda x:x[1],reverse=True)
        # return ([key for key,value in result_items])
        # rresult.keys()
        names_and_hights=[]
        for i in range(len(names)):
            names_and_hights.append([names[i] ,heights[i]])
        names_and_hights.sort(key=lambda x:x[1],reverse=True)
        return ([i[0] for i in names_and_hights])
        