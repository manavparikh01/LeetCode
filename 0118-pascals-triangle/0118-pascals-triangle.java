class Solution {
    public List<List<Integer>> generate(int numRows) {
        if (numRows == 0)
        {
            return new ArrayList<>();
        }
        List<List<Integer>> al = new ArrayList<>();
        List<Integer> am = new ArrayList<>();
        List<Integer> as = new ArrayList<>();
        am.add(1);
        as.add(1);
        al.add(am);
        if (numRows == 1)
        {
            return al;
        }
        as.add(1);
        al.add(as);
        if (numRows == 2)
        {
            return al;
        }
        for (int j = 3;j<=numRows;j++)
        {
            List<Integer> ss = new ArrayList<Integer>();
            int a = 0;
            //int prev = 0;
            ss.add(as.get(0));
            for (int i = 1;i<as.size();i++)
            {
                a = as.get(i-1) + as.get(i);
                ss.add(a);
            }
            ss.add(as.get(al.size() - 1));
            al.add(ss);
            as = ss;
        }
        return al;
    }
}