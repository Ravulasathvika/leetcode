class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num=[]
        num=nums1+nums2
        num.sort()
        n=len(num)
        if n % 2 == 0:
            m1 = n // 2 - 1
            m2 = n // 2
            median = (num[m1] + num[m2]) / 2.0  
            return median
        else:
            m=n//2
            median=num[m]
            return median
        