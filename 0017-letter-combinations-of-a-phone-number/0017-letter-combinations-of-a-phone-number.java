class Solution {
    public List<String> l;
    public String s;
    public int i;
    public HashMap<Character, String> hm;
    
    public List<String> letterCombinations(String digits) {
        l = new ArrayList<>();
        s = "";
        i = 0;
        hm = new HashMap<>();
        hm.put('2', "abc");
        hm.put('3', "def");
        hm.put('4', "ghi");
        hm.put('5', "jkl");
        hm.put('6', "mno");
        hm.put('7', "pqrs");
        hm.put('8', "tuv");
        hm.put('9', "wxyz");
        if (digits.length() == 0)
        {
            return l;
        }
        
        doCombinations(digits);
        return l;
    }
    
    public void doCombinations(String digits)
    {
        if (s.length() == digits.length())
        {
            l.add(s);
            return;
        }
        String a = hm.get(digits.charAt(i));
        for (int j = 0; j<a.length();j++)
        {
            s = s + a.charAt(j);
            i++;
            doCombinations(digits);
            
            s = s.substring(0, s.length() - 1);
            i--;
        }
    }
}