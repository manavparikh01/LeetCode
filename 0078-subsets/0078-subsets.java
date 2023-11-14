class Solution {
    public List<Integer> l;
    public List<List<Integer>> ll;
    
    public List<List<Integer>> subsets(int[] nums) {
        l = new ArrayList<>();
        ll = new ArrayList<>();
        allSets(nums, 0);
        return ll;
    }
    
    public void allSets(int[] nums, int i)
    {
        if (i >= nums.length)
        {
            System.out.println(l.size());
            ll.add(new ArrayList<>(l));
            return;
        }
        
        
        l.add(nums[i]);
        allSets(nums, i + 1);
        
        l.remove(l.size() - 1);
        allSets(nums, i + 1);
    }
}