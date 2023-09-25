class Solution {
    String s = "";
    List<String> l = new ArrayList<String>();
    public List<String> generateParenthesis(int n) {
        int open = 0;
        int close = 0;
        backTrack(open, close, n);
        return l;
    }

    public void backTrack(int open, int close, int n) {
        if (open == n && close == n)
        {
            l.add(s);
            return;
        }
        if (open < n)
        {
            s = s + '(';
            backTrack(open + 1, close, n);
            s = s.substring(0, s.length() - 1);
        }
        if (close < open)
        {
            s = s + ')';
            backTrack(open, close + 1, n);
            s = s.substring(0, s.length() - 1);
        }
    }
}