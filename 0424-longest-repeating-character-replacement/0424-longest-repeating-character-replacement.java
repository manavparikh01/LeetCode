class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        int l = 0;
        int res = 0;
        int max = 1;
        for (int r = 0;r<s.length();r++)
        {
            if (!hm.containsKey(s.charAt(r)))
            {
                hm.put(s.charAt(r), 1);
            }
            else
            {
                hm.put(s.charAt(r), hm.get(s.charAt(r)) + 1);
                max = Math.max(max, hm.get(s.charAt(r)));
            }
            while ((r-l+1) - max > k)
            {
                hm.put(s.charAt(l), hm.get(s.charAt(l)) - 1);
                l++;
            }
            res = Math.max(res, (r-l+1));
        }
        return res;
    }
}