class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int max=0;
        int count=0;
        for (int i=0;i<rectangles.length;i++)
        {
            int min=0;
            if (rectangles[i][0] < rectangles[i][1])
            {
                min = rectangles[i][0];
            } else {
                min = rectangles[i][1];
            }
            System.out.print(count);
            if (min==max)
            {
                count++;
            }
            if (min>max)
            {
                max=min;
                count=1;
            }
            
            
        }
        return count;
    }
}