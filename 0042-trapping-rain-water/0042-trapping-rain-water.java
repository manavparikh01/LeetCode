class Solution {
    public int trap(int[] height) {
        int l = 0;
        int h = height.length - 1;
        int left = height[l];
        int right = height[h];
        int sum = 0;
        while (l < h)
        {
            if (left <= right)
            {
                l++;
                left = Math.max(left, height[l]);
                sum += left - height[l];
            }
            else
            {
                h--;
                right = Math.max(right, height[h]);
                sum += right - height[h];
            }
        }
        return sum;
    }
}