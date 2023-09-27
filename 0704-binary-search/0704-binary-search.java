class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 1)
        {
            if (nums[0] == target)
            {
                return 0;
            }
            return -1;
        }
        int l = 0;
        int h = nums.length - 1;
        while (l <= h)
        {
            int mid = (h - l)/2 + l;
            if (nums[mid] == target)
            {
                return mid;
            }
            else if (nums[mid] < target)
            {
                l = mid + 1;
            }
            else
            {
                h = mid - 1;
            }
        }
        return -1;
    }
}