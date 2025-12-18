class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalgas = sum(gas)
        totalcost = sum(cost)
        if totalgas<totalcost: return -1
        ans = 0
        remain = 0
        for i in range(len(gas)):
            remain += gas[i]-cost[i]
            if remain<0:
                remain = 0
                ans = i+1
        return ans