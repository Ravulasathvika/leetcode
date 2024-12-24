class Solution {
    public int[] runningSum(int[] nums) {
        int index=0;
        int prevsum=0;
        for(int i=0;i<nums.length;i++)
        {
            prevsum+=nums[i];
            nums[index]=prevsum;
            index++;
        }
        return nums;
        
    }
}