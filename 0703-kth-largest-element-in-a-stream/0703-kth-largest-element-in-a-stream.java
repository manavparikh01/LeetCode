class KthLargest {
    public PriorityQueue<Integer> pq;
    public int value = 0;

    public KthLargest(int k, int[] nums) {
        pq = new PriorityQueue<Integer>();
        value = k;
        for (int i = 0;i<nums.length;i++)
        {
            if (i >= k)
            {
                if (nums[i] > pq.peek())
                {
                    pq.remove();
                    pq.add(nums[i]);
                }
            }
            else
            {
                pq.add(nums[i]);
            }
        }
    }
    
    public int add(int val) {
        if (pq.size() < value)
        {
            pq.add(val);
        }
        else
        {
            if (val > pq.peek())
            {
                pq.remove();
                pq.add(val);
            }
        }
        if (value > pq.size())
        {
            return -1;
        }
        return pq.peek();
    }

}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */