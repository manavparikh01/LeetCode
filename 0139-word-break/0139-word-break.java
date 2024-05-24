class Solution {
    boolean done = false;
    HashSet<Integer> hs = new HashSet<Integer>();
    public boolean wordBreak(String s, List<String> wordDict) {
        dp(s, 0, 1, wordDict);
        return done;
    }
    
    public void dp(String s, int a, int b, List<String> wordDict)
    {
        if ((wordDict.contains(s.substring(a,b)) && b == s.length()) || done == true)
        {
            done = true;
            return;
        }
        if (b==s.length())
        {
            hs.add(a);
            return;
        }
        if (hs.contains(a))
        {
            return;
        }
        if (wordDict.contains(s.substring(a,b)))
        {
            dp(s,b,b+1,wordDict);
        }
        // System.out.println(s.substring(a,b))
        dp(s,a,b+1,wordDict);
        return;
    }
}