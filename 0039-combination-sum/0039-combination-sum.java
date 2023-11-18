class Solution {
    public List<List<Integer>> l;
    public List<Integer> ll;
    public HashMap<Integer, Integer> hm;
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        l = new ArrayList<>();
        ll = new ArrayList<>();
        // Arrays.sort(candidates);
        // hm = new HashMap<>();
        // for (int i = 0;i<candidates.length;i++)
        // {
        //     hm.put(candidates[i], i);
        // }
        doCombinations(candidates, target, 0, 0);
        return l;
    }
    
    public void doCombinations(int[] candidates, int target, int i, int sum)
    {
        if (sum == target)
        {
            l.add(new ArrayList<>(ll));
            return;
        }
        if (i == candidates.length || sum > target)
        {
            return;
        }
        ll.add(candidates[i]);
        doCombinations(candidates, target, i, sum + candidates[i]);
        
        ll.remove(ll.size() - 1);
        doCombinations(candidates, target, i+1, sum);
    }
}