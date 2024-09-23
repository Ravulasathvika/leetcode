class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result=[]
        i=0
        result.append(intervals[0])
        for interval in intervals:
            if result[i][1]>interval[1]:
                continue
            elif result[i][1]>=interval[0]:
                result[i][1]=interval[1]
            else:
                result.append(interval)
                i+=1
        return result