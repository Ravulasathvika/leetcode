class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> list=new ArrayList<>();
        solve(nums,list,new ArrayList<>());
        return list;
        
    }
    public void solve(int[] nums,List<List<Integer>> list,List<Integer> templist)
    {
        
        if(templist.size()==nums.length)
        {
            list.add(new ArrayList<>(templist));
            return;
        }
        else
        {
            for(int i=0;i<nums.length;i++)
            {
                if(templist.contains(nums[i])) continue;
                templist.add(nums[i]);
                solve(nums,list,templist);
                templist.remove(templist.size()-1);
            }
        }
        
        
    }
}