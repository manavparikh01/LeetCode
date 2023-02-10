class Solution {
    public String replaceDigits(String s) {
        String sm = "";
        for (int i=0;i<s.length();i++)
        {
            if (i % 2 != 0)
            {
                int m = (int)s.charAt(i-1) + (int)(s.charAt(i) - '0');
                //System.out.println(m);
                String n = Character.toString((char)m);
                sm = sm + n;
            }
            else
            {
                sm = sm + s.charAt(i);
            }
        }
        return sm;
    }
}