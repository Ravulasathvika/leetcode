class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        if n==0 or n==1:
            return n
        else:
            for i in range(1,n+1):
                c=a+b
                a=b
                b=c
            return b