class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        if (position.length == 1)
        {
            return 1;
        }
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for (int i = 0;i<position.length;i++)
        {
            hm.put(position[i], speed[i]);
        }
        TreeMap<Integer, Integer> t = new TreeMap<Integer, Integer>();
        t.putAll(hm);
        int n = 0;
        for (Map.Entry<Integer, Integer> entry: t.entrySet())
        {
            position[n] = entry.getKey();
            speed[n] = entry.getValue();
            n++;
        }
        Stack<Double> st = new Stack<Double>();
        double ti = ((double)target - (double)position[position.length - 1])/(double)speed[position.length - 1];
        st.push(ti);
        for (int i = position.length - 2; i>=0;i--)
        {
            double time = ((double)target - (double)position[i])/(double)speed[i];
            if (time > st.peek())
            {
                st.push(time);
            }
        }
        return st.size();
    }
}