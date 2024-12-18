class Solution {
    public int lengthOfLIS(int[] nums) {
        if(nums==null || nums.length==0)return 0;
        int n=nums.length;
        int dp[]=new int[n];
        Arrays.fill(dp,1);
        int max_length=1;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                if(nums[j]<nums[i])
                {
                    dp[i]=Math.max(dp[i],dp[j]+1);
                    
                }
                
            }
            max_length=Math.max(max_length,dp[i]);
        }
        return max_length;
        
    }        
    
}