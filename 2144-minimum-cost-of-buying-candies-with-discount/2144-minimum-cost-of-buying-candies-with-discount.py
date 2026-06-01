class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n=len(cost)
        result=0
        if len(cost)<=2:
            return sum(cost)
        cost.sort(reverse=True)
        for i in range(0,n,3):
            if n-i<3:
                result+=sum(cost[i:])
            else:
                result+=cost[i]+cost[i+1]
        return result