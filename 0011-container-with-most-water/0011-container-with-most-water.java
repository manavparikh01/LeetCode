class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int area = 0;
        while (left < right)
        {
            int a = min(height[left], height[right]) * (right - left);
            area = max(area, a);
            if (height[left] < height[right])
            {
                left += 1;
            }
            else
            {
                right -= 1;
            }
        }
        return area;
    }
    
    public int min(int a, int b)
    {
        if (a < b)
        {
            return a;
        }
        return b;
    }
    
    public int max(int a, int b)
    {
        if (a > b)
        {
            return a;
        }
        return b;
    }
}