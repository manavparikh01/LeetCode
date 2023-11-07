class Solution {
    public int[][] kClosest(int[][] points, int k) {
        HashMap<Double, ArrayList<int[]>> hm = new HashMap<Double, ArrayList<int[]>>();
        PriorityQueue<Double> p = new PriorityQueue<Double>();
        int[][] arr = new int[k][2];
        for (int i = 0;i<points.length;i++)
        {
            double c = (double)Math.pow(points[i][0],2) + (double)Math.pow(points[i][1],2);
            //System.out.println(i + " " + c);
            if (hm.containsKey(c))
            {
                ArrayList<int[]> alll = hm.get(c);
                alll.add(points[i]);
                hm.put(c, alll);
            }
            else
            {
                ArrayList<int[]> al = new ArrayList<int[]>();
                al.add(points[i]);
                hm.put(c, al);
            }
        }
        for (Map.Entry<Double, ArrayList<int[]>> e : hm.entrySet())
        {
            //System.out.println(e.getKey());
            p.add(e.getKey());
        }
        int i = 0;
        int j = 0;
        int size = p.size();
        while (j < size && i < k)
        {
            double a = p.peek();
            p.remove();
            //System.out.println(a);
            ArrayList<int[]> all = hm.get(a);
            while (all.size() > 0)
            {
                arr[i] = all.get(0);
                all.remove(0);
                i++;
            }
            j++;
        }
        return arr;
    }
}