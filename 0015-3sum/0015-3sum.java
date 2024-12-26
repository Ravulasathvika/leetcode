class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res=new ArrayList<>();
        Arrays.sort(nums);
        int n=nums.length;
        for(int i=0;i<n;i++)
        {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int a=nums[i];
            int target=-a;
            int start=i+1;
            int end=n-1;
            while(start<end)
            {
                int sum=nums[start]+nums[end];
                if(sum==target)
                {
                    res.add(Arrays.asList(nums[i],nums[start],nums[end]));
                    while (start < end && nums[start] == nums[start + 1]) {
                        start++;
                    }
                    while (start < end && nums[end] == nums[end - 1]) {
                        end--;
                    }

                    
                    start++;
                    end--;
                }
                else if(sum>target)
                {
                    end--;
                }
                else
                {
                    start++;
                }
            }
        }
        return res;
    }
    
}