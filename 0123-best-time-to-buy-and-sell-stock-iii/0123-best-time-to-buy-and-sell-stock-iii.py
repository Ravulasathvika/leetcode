class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      initial=0
      bought1=-inf
      sold1=0
      bought2=-inf
      sold2=0
      for x in prices:
        bought1=max(initial-x,bought1)
        sold1=max(bought1+x,sold1)
        bought2=max(sold1-x,bought2)
        sold2=max(bought2+x,sold2)
      return sold2
        