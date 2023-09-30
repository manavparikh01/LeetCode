class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int h = nums.length - 1;
        while (l <= h)
        {
            int mid = (h - l)/2 + l;
            if (nums[mid] == target)
            {
                return mid;
            }
            if (nums[mid] >= nums[l])
            {
                if (nums[mid] < target || nums[l] > target)
                {
                    l = mid + 1;
                }
                else
                {
                    h = mid - 1;
                }
            }
            else
            {
                if (nums[mid] > target || target > nums[h])
                {
                    h = mid - 1;
                }
                else
                {
                    l = mid + 1;
                }
            }
        }
        return -1;
    }
}