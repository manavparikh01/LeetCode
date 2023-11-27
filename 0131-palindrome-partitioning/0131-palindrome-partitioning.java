class Solution {
    public List<List<String>> l;
    // public List<String> ll;
    
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<List<String>>();
        if (s.equals("")) {
            res.add(new ArrayList<String>());
            return res;
        }
        for (int i = 0; i < s.length(); i++) {
            if (isPalindrome(s, i + 1)) {
                for (List<String> list : partition(s.substring(i + 1))) {
                    list.add(0, s.substring(0, i + 1));
                    res.add(list);
                }
            }
        }
        return res;
    }
    
//     public void doPartition(String s, int i)
//     {
//         if (i > s.length())
//         {
//             l.add(new ArrayList<>(ll));
//         }
        
//         for (int j=i;j<s.length();j++)
//         {
//             if (isPalindrome(s.substring(i,j+1)))
//             {
//                 ll.add(s.substring(i,j+1));
//                 doPartition(s.substring(i, j+1), j+1);
//                 ll.remove(ll.size() - 1);    
//             }
//         }
//     }
    
    public boolean isPalindrome(String s, int n)
    {
        for (int i = 0;i<n/2;i++)
        {
            if (s.charAt(i) != s.charAt(n-i-1))
            {
                return false;
            }
        }
        return true;
    }
    
    // public boolean isPalindrome(String s)
    // {
    //     int length = s.length();
    //     String re = "";
    //     for (int i = length-1;i>=0;i--)
    //     {
    //         re = re + s.charAt(i);
    //     }
    //     if (re.equals(s))
    //     {
    //         return true;
    //     }
    //     return false;
    // }
}