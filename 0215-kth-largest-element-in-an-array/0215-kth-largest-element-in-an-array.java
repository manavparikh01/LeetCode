class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> p = new PriorityQueue<Integer>();
        for (int i = 0;i<nums.length;i++)
        {
            if (p.size() < k)
            {
                p.add(nums[i]);
            }
            else
            {
                if (nums[i] <= p.peek())
                {
                    
                }
                else
                {
                    p.add(nums[i]);
                    p.remove();
                }
            }
        }
        int a = p.peek();
        return a;
    }
}