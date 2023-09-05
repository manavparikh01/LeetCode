class Solution {
    public boolean isPalindrome(String s) {
        Stack<Character> al = new Stack<Character>();
        String ss = s.toLowerCase();
        for (int i = 0;i<s.length();i++)
        {
            if ((ss.charAt(i) >= 'a' && ss.charAt(i) <= 'z') || (ss.charAt(i) >= '0' && ss.charAt(i) <= '9'))
            {
                al.push(ss.charAt(i));
            }
        }
        // while (!al.isEmpty())
        // {
        //     System.out.print(al.pop());
        // }
        for (int i = 0;i<s.length();i++)
        {
            if ((ss.charAt(i) >= 'a' && ss.charAt(i) <= 'z') || (ss.charAt(i) >= '0' && ss.charAt(i) <= '9'))
            {
                if (ss.charAt(i) != al.peek())
                {
                    return false;
                }
                al.pop();
            }
        }
        if (al.size() != 0)
        {
            return false;
        }
        return true;
    }
}