class Solution {
    public List<List<Integer>> l;
    public List<Integer> ll;
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        l = new ArrayList<>();
        ll = new ArrayList<>();
        findSubsets(nums, 0);
        return l;
    }
    
    public void findSubsets(int[] nums, int i)
    {
        if (i == nums.length)
        {
            List<Integer> lll = new ArrayList<>(ll);
            Collections.sort(lll);
            if (!l.contains(lll))
            {
                l.add(new ArrayList<>(lll));
            }
            return;
        }
        
        ll.add(nums[i]);
        findSubsets(nums, i+1);
        
        ll.remove(ll.size() - 1);
        findSubsets(nums, i+1);
    }
}