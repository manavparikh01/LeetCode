class Solution {
    
    public class Pair {
        int pcount;
        int timecount;
        public Pair(int a, int b)
        {
            pcount = a;
            timecount = b;
        }
    }
    
    public int leastInterval(char[] tasks, int n) {
        if (n == 0)
        {
            return tasks.length;
        }
        HashMap<Character, Integer> h = new HashMap<Character, Integer>();
        PriorityQueue<Integer> p = new PriorityQueue<Integer>(Collections.reverseOrder());
        Deque<Pair> d = new ArrayDeque<Pair>();
        for (int i = 0;i<tasks.length;i++)
        {
            if (h.containsKey(tasks[i]))
            {
                int a = h.get(tasks[i]);
                a += 1;
                h.put(tasks[i], a);
            }
            else
            {
                h.put(tasks[i], 1);
            }
        }
        for (Map.Entry<Character, Integer> e : h.entrySet())
        {
            p.add(e.getValue());
        }
        int time = 1;
        int b = p.peek();
        p.remove();
        if (b > 1)
        {
            d.addFirst(new Pair(b-1,time+n+1));
        }
        while (p.isEmpty() == false || d.isEmpty() == false)
        {
            time += 1;
            if (d.isEmpty() == false)
            {
                Pair pa = d.getFirst();
                if (time == pa.timecount)
                {
                    //System.out.println(pa.pcount + " " + time + " " + pa.timecount);
                    p.add(pa.pcount);
                    d.removeFirst();
                }
            }
            if (p.size() == 0)
            {
                
            }
            else
            {
                int bb = p.peek();
                p.remove();
                if (bb > 1)
                {
                    d.addLast(new Pair(bb-1,time+n+1));
                }
            }
        }
        //System.out.println(d.size());
        return time;
    }
}