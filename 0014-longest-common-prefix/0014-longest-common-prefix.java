class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0 || strs[0].length() == 0)
        {
            return "";
        }
        String s = strs[0];
        for (int i = 1;i<strs.length;i++)
        {
            while (strs[i].indexOf(s) != 0)
            {
                s = s.substring(0, s.length() -1);
            }
        }
        return s;
        // String s = "";
        // int l = 0;
        // for (int i = 0;i<strs.length;i++)
        // {
        //     i = Math.min(l, strs[i].length());
        // }
        // for (int i = 0;i<l;i++)
        // {
        //     char c = strs[0].charAt(i);
        //     boolean m = true;;
        //     for (int j = 1;j<strs.length;j++)
        //     {
        //         if (strs[j].charAt(i) != c)
        //         {
        //             m = false;
        //             break;
        //         }
        //     }
        //     if (m)
        //     {
        //         s = s + String.valueOf(c);
        //     }
        //     else
        //     {
        //         break;
        //     }
        // }
        // return s;
    }
}