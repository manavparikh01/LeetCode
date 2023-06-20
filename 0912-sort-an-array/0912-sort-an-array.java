class Solution {
    public int[] sortArray(int[] nums) {
        heapSort(nums, nums.length);
        return nums;
    }
    
    public void heapSort(int[] nums, int n)
    {
        buildHeap(nums, n);
        for (int i = n-1;i>=1;i--)
        {
            int temp = nums[0];
            nums[0] = nums[i];
            nums[i] = temp;
            maxHeapify(nums, i, 0);
        }
    }
    
    public void buildHeap(int[] nums, int n)
    {
        for (int i = (n-2)/2;i>=0;i--)
        {
            maxHeapify(nums, n, i);
        }
    }
    
    public void maxHeapify(int[] nums, int n, int i)
    {
        int largest = i;
        int left = 2*i+1;
        int right = 2*i+2;
        if (left<n && nums[left] > nums[largest])
        {
            largest=left;
        }
        if (right<n && nums[right] > nums[largest])
        {
            largest=right;
        }
        if (largest != i)
        {
            int temp = nums[largest];
            nums[largest] = nums[i];
            nums[i] = temp;
            maxHeapify(nums, n, largest);
        }
    }
}