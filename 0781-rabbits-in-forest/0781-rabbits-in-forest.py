class Solution(object):
    def numRabbits(self, answers):
        # zero_count=answers.count(0)-1
        # answers=set(answers)
        # return sum(answers)+len(answers)+zero_count if 0 in answers else sum(answers)+len(answers)
        """
        :type answers: List[int]
        :rtype: int
        """
        freq=Counter(answers)
        total=0
        for i, count in freq.items():
            gs=i+1
            groups=(count+gs-1)//gs
            total+=groups*gs
        return total
        