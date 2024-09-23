class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub=nums[0]
        curr_sum=0
        for i in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=i
            max_sub=max(max_sub,curr_sum)
        return max_sub