class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length())
        {
            return false;
        }
        HashMap<Character, Character> hm = new HashMap<Character, Character>();
        for (int i = 0; i<s.length();i++)
        {
            if (!hm.containsKey(s.charAt(i)))
            {
                if (t.indexOf(t.charAt(i)) < i)
                {
                    return false;
                }
                hm.put(s.charAt(i), t.charAt(i));
            }
            else
            {
                if (hm.get(s.charAt(i)) != t.charAt(i))
                {
                    return false;
                }
            }
        }
        return true;
    }
}