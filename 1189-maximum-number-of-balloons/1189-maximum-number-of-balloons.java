class Solution {
    public int maxNumberOfBalloons(String text) {
        if (text.length() == 0 || text.length() < 7)
        {
            return 0;
        }
        //HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        int b = 0, a = 0, l = 0, o = 0,n = 0;
        for (int i = 0;i<text.length();i++)
        {
            if (text.charAt(i) == 'b')
            {
                b++;
            }
            if (text.charAt(i) == 'a')
            {
                a++;
            }
            if (text.charAt(i) == 'l')
            {
                l++;
            }
            if (text.charAt(i) == 'o')
            {
                o++;
            }
            if (text.charAt(i) == 'n')
            {
                n++;
            }
        }
        //System.out.println("b" + b + " a" + a + " l" + l + " o" + o + " n" + n);
        int i = 0;
        while (b >= 1 && a >= 1 && l >= 2 && o >= 2 && n >= 1)
        {
            i++;
            b--; a--; l -= 2; o -= 2; n--;
        }
        return i;
    }
}