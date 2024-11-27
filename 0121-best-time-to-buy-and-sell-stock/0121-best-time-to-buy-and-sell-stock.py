class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxProfit=0
        minParchase=prices[0]
        for i in range(1,len(prices)):
            maxProfit=max(maxProfit,prices[i]-minParchase)
            minParchase=min(minParchase,prices[i])
        return maxProfit