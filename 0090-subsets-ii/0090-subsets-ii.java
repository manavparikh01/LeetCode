class Solution {
    public List<List<Integer>> l;
    public List<Integer> ll;
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        l = new ArrayList<>();
        ll = new ArrayList<>();
        Arrays.sort(nums);
        findSubsets(nums, 0);
        return l;
    }
    
    public void findSubsets(int[] nums, int i)
    {
        if (i == nums.length)
        {
            l.add(new ArrayList<>(ll));
            return;
        }
        
        ll.add(nums[i]);
        findSubsets(nums, i+1);
        
        ll.remove(ll.size() - 1);
        while (i+1 < nums.length && nums[i] == nums[i+1])
        {
            i++;
        }
        findSubsets(nums, i+1);
    }
}