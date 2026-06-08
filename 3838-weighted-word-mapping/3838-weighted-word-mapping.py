class Solution(object):
    def mapWordWeights(self, words, weights):
        dic={}
        ind=0
        for i in range(97,122+1):
            dic[chr(i)]=weights[ind]
            ind+=1
        # print(dic)
        result=""
        for i in words:
            tr=0
            for j in i:
                tr+=dic[j]
            result+=chr(123-((tr%26)+1))
            # print(123-(tr%26))
            print(tr)
            print(result)
        return result 
        # wholewords=""
        # result=""
        # for i in words:
        #     for j in i:
        #         wholewords+=j
        # for i
        # result.append(wholewords[])
        # for i in words:
        # words=words()
        # for i in words:
        #     if
           
                
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        