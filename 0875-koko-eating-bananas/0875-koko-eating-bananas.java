class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int l = piles.length;
        int a = 1;
        int b = piles[l - 1];
        int mid1 = b;
        while (a <= b)
        {
            int mid = (b + a)/2;
            int m = 0;
            for (int i = 0;i<l;i++)
            {
                m += Math.ceil((double)piles[i]/mid);
            }
            if (m <= h)
            {
                mid1 = Math.min(mid1, mid);
                b = mid - 1;
            }
            else
            {
                a = mid + 1;
            }
        }
        return mid1;
    }
}