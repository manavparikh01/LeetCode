class MedianFinder {
    public int size;
    public PriorityQueue<Integer> maxpq;
    public PriorityQueue<Integer> minpq;

    public MedianFinder() {
        size = 0;
        maxpq = new PriorityQueue<Integer>(Collections.reverseOrder());
        minpq = new PriorityQueue<Integer>();
    }
    
    public void addNum(int num) {
        if (size == 0)
        {
            maxpq.add(num);
            size++;
        }
        else
        {
            if (size%2 == 0)
            {
                if (num < minpq.peek())
                {
                    maxpq.add(num);
                }
                else
                {
                    int a = minpq.poll();
                    minpq.add(num);
                    maxpq.add(a);
                }
                size++;
            }
            else
            {
                if (num > maxpq.peek())
                {
                    minpq.add(num);
                }
                else
                {
                    int a = maxpq.poll();
                    maxpq.add(num);
                    minpq.add(a);
                }
                size++;
            }
        }
        
    }
    
    public double findMedian() {
        double c;
        if (size%2 == 0)
        {
            c = (double)(maxpq.peek() + minpq.peek())/2;
        }
        else
        {
            c = (double)maxpq.peek();
        }
        return c;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */