class Solution {
    public int maxProduct(int[] nums) {
        int max_sum=nums[0];
        int curr_max=nums[0];
        int curr_min=nums[0];
        for(int i=1;i<nums.length;i++)
        {
            int num=nums[i];
            int temp_max=Math.max(num,Math.max(num*curr_max,num*curr_min));
            int temp_min=Math.min(num,Math.min(num*curr_max,num*curr_min));
            curr_max=temp_max;
            curr_min=temp_min;                  
            max_sum=Math.max(curr_max,max_sum);                  
        }
        return max_sum;
        
        
        
    }
}