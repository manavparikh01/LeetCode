class Solution {
    public boolean wordPattern(String pattern, String s) {
        HashMap<Character, String> hm = new HashMap<Character, String>();
        int m = 0;
        int n = 0;
        for (int i = 0;i<pattern.length();i++)
        {
            while (n<s.length() && s.charAt(n) != ' ')
            {
                n++;
            }
            //System.out.print(m + " " + n);
            if (n > s.length())
            {
                return false;
            }
            String ss = s.substring(m, n);
            //System.out.println(ss);
            if (hm.containsKey(pattern.charAt(i)))
            {
                String an = hm.get(pattern.charAt(i));
                if (!an.equals(ss))
                {
                    return false;
                }
            }
            else
            {
                if (hm.containsValue(ss))
                {
                    return false;
                }
                hm.put(pattern.charAt(i), ss);
            }
            m = n;
            m++;
            n++;
        }
        if (n < s.length())
        {
            return false;
        }
        return true;
    }
}