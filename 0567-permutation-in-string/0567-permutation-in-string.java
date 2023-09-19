class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s2.length() < s1.length())
        {
            return false;
        }
        HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        HashMap<Character, Integer> hmm = new HashMap<Character, Integer>();
        for (int i = 0;i<s1.length();i++)
        {
            if (hm.containsKey(s1.charAt(i)))
            {
                hm.put(s1.charAt(i), hm.get(s1.charAt(i)) + 1);
            }
            else
            {
                hm.put(s1.charAt(i), 1);
            }
        }
        int l = 0;
        int r = s1.length();
        for (int i = 0; i<s1.length();i++)
        {
            if (hmm.containsKey(s2.charAt(i)))
            {
                hmm.put(s2.charAt(i), hmm.get(s2.charAt(i)) + 1);
            }
            else
            {
                hmm.put(s2.charAt(i), 1);
            }
        }
        if (hm.equals(hmm))
        {
            return true;
        }
        while (r < s2.length())
        {
            if (l != r)
            {
            if (hmm.get(s2.charAt(l)) == 1)
            {
                hmm.remove(s2.charAt(l));
            }
            else
            {
                hmm.put(s2.charAt(l), hmm.get(s2.charAt(l)) - 1);
            }
                if (hmm.containsKey(s2.charAt(r)))
            {
                hmm.put(s2.charAt(r), hmm.get(s2.charAt(r)) + 1);
            }
            else
            {
                hmm.put(s2.charAt(r), 1);
            }
            }
            l++;
            r++;
            if (hm.equals(hmm))
            {
                return true;
            }
        }
        return false;
    }
}