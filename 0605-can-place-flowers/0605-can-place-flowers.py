class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count=0
        prev=-2
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                count+=(i-prev-2)//2
                prev=i
        count+=(len(flowerbed)-prev-1)//2
        if count>=n:
            return True
        else:
            return False
        