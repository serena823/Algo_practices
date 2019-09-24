class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gas_gain = sum(gas)
        gas_cost = sum(cost)
        if gas_gain < gas_cost:
            return -1
        res = 0
        index = 0
        for i in range(len(gas)):
            diff = gas[i] + res - cost[i]
            if diff < 0:
                res = 0
                index = i + 1
            else:
                res = diff
        return index
         
            
            
        