class Solution {
    public int maxProduct(int[] nums) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        int sum=1;
        for (int i=0;i<nums.length;i++)
        {
            minHeap.add(nums[i]);
            if (minHeap.size() > 2)
            {
                minHeap.remove();
            }
        }
        //System.out.println(minHeap.size());
        while (minHeap.size() > 0)
        {
            int i = minHeap.poll();
            //System.out.println(i);
            sum *= (i-1); 
        }
        return sum;
        
    }
}