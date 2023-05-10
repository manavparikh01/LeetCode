class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> hs = new HashSet<String>();
        for (int i = 0;i<emails.length;i++)
        {
            char c[] = emails[i].toCharArray();
            int j = 0;
            int index = emails[i].indexOf("@");
            String str = "";
            if (index == 0 || index == -1)
            {
                continue;
            }
            for (int m = 0;m<index;m++)
            {
                if (c[m] == '+')
                {
                    break;
                }
                if (c[m] == '.')
                {
                    
                }
                else
                {
                    str = str + String.valueOf(c[m]);
                }
            }
            for (int m = index;m<emails[i].length();m++)
            {
                str = str + String.valueOf(c[m]);
            }
            hs.add(str);
        }
        return hs.size();
    }
}