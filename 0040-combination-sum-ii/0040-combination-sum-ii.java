class Solution {
    public List<List<Integer>> l;
    public List<Integer> ll;
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        l = new ArrayList<>();
        ll = new ArrayList<>();
        Arrays.sort(candidates);
        doCombinationsSum(candidates, target, 0, 0);
        return l;
    }
    
    public void doCombinationsSum(int[] candidates, int target, int i, int sum)
    {
        if (sum == target)
        {
            l.add(new ArrayList<>(ll));
            return;
        }
        if (sum > target)
        {
            return;
        }
        if (i == candidates.length)
        {
            return;
        }
        
        ll.add(candidates[i]);
        doCombinationsSum(candidates, target, i + 1, sum + candidates[i]);
        
        ll.remove(ll.size() - 1);
        while (i + 1 < candidates.length && candidates[i] == candidates[i+1])
        {
            i++;
        }
        doCombinationsSum(candidates, target, i + 1, sum);
    }
}