class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int h = nums.length - 1;
        int min = Integer.MAX_VALUE;
        while (l <= h)
        {
            int mid = (h - l)/2 + l;
            min = Math.min(min, nums[mid]);
            if (nums[mid] < nums[h])
            {
                h = mid - 1;
            }
            else
            {
                l = mid + 1;
            }
        }
        return min;
    }
}