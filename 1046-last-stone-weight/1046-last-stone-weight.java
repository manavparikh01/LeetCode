class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> p = new PriorityQueue<Integer>(Collections.reverseOrder());
        for (int i = 0;i<stones.length;i++)
        {
            p.add(stones[i]);
        }
        while (p.size() > 1)
        {
            int a = p.peek();
            p.remove();
            int b = p.peek();
            p.remove();
            int c = a - b;
            System.out.println(c + " " + a + " " +  " " + b);
            if (c != 0)
            {
                p.add(c);
            }
        }
        if (p.size() == 0)
        {
            return 0;
        }
        return p.peek();
    }
}