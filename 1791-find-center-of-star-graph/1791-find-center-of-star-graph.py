class Solution(object):
    def findCenter(self, edges):
        dfa=edges[0]
        dfa.extend(edges[1])
        for i in dfa:
            if dfa.count(i)==2:
                return i
                
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        