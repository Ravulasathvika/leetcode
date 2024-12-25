class Solution {
    public int majorityElement(int[] nums) {
        int majority_ele=0;
        int count=0;
        for(int i=0;i<nums.length;i++)
        {
            if(count==0)
            {
                majority_ele=nums[i];
                
            }
            if(nums[i]==majority_ele)
            {
                count+=1;
            }
            else
            {
                count-=1;
            }
        }
        return majority_ele;
        
    }
}