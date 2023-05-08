class Solution {
    public int lengthOfLastWord(String s) {
        String a = s.trim();
        int l = a.length()-1;
        int num = 0;
        while (l>=0 && a.charAt(l) != ' ')
        {
            num++;
            l--;
        }
        return num;
    }
}