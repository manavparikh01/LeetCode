class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int l = matrix.length - 1;
        int h = matrix[0].length - 1;
        int l1 = 0;
        int l2 = matrix.length - 1;
        int h1 = 0;
        int h2 = matrix[0].length - 1;
        while (l1 <= l2 && h1 <= h2)
        {
            int midl = (l2 - l1)/2 + l1;
            int midh = (h2 - h1)/2 + h1;
            //System.out.println(matrix[midl][midh]);
            if (matrix[midl][midh] == target)
            {
                return true;
            }
            else if (matrix[midl][midh] < target)
            {
                if (matrix[midl][h] == target)
                {
                    return true;
                }
                else if (matrix[midl][h] > target)
                {
                    l1 = midl;
                    h1 = midh + 1;
                    l2 = midl;
                }
                else
                {
                    l1 = midl + 1;
                    h1 = 0;
                }
            }
            else
            {
                if (matrix[midl][0] == target)
                {
                    return true;
                }
                else if (matrix[midl][0] > target)
                {
                    l2 = midl - 1;
                    h2 = h;
                }
                else
                {
                    l2 = midl;
                    h2 = midh - 1;
                    l1 = midl;
                }
            }
        }
        return false;
    }
}