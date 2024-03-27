class Solution {
    public int countSubstrings(String s) {
        int l = s.length();
        if (l < 2)
        {
            return 1;
        }
        int count = 0;
        for (int i = 0;i<l;i++)
        {
            int left = i;
            int right = i;
            while (left>= 0 && right<l && s.charAt(left) == s.charAt(right))
            {
                count++;
                left -= 1;
                right += 1;
            }
            
            left = i;
            right = i+1;
            while (left>= 0 && right<l && s.charAt(left) == s.charAt(right))
            {
                count++;
                left -= 1;
                right += 1;
            }
        }
        return count;
    }
}