class Solution {
    int count = 0;
    HashMap<Integer, Integer> hm;
    public int climbStairs(int n) {
        hm = new HashMap<>();
        dfs(0, n);
        return count;
    }
    
    public void dfs(int i, int n)
    {
        if (i == n)
        {
            count++;
            return;
        }
        if (i > n)
        {
            return;
        }
        if (hm.containsKey(i))
        {
            count += hm.get(i);
            return;
        }
        dfs(i+1, n);
        
        dfs(i+2, n);
        hm.put(i, count);
        return;
    }
}