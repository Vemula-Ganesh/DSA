class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # st=tank=dif=0
        # for i in range(len(gas)):
        #     tank+=gas[i]-cost[i]
        #     dif+=gas[i]-cost[i]
        #     if tank<0:
        #         st=i+1
        #         tank=0
        # return -1 if dif<0 else st

        if sum(gas)<sum(cost):return -1
        st=tank=0
        for i in range(len(gas)):
            tank+=gas[i]-cost[i]
            if tank<0:
                st=i+1
                tank=0
        return st