class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0)
        {
            return 0;
        }
        if (s.length() == 1)
        {
            return 1;
        }
        HashMap<Character, Integer> hs = new HashMap<Character, Integer>();
        int length = 0;
        int l = 0;
        hs.put(s.charAt(l), l);
        for (int r = 1; r<s.length();r++)
        {
            while (hs.containsKey(s.charAt(r)))
            {
                hs.remove(s.charAt(l));
                l++;
            }
            //int le = 0;
            // while (r < s.length() && !hs.containsKey(s.charAt(r)))
            // {
            //     hs.put(s.charAt(r),r);
            //     r++;
            // }
            hs.put(s.charAt(r), r);
            length = Math.max(length, r - l + 1);
        }
        return length;
    }
}