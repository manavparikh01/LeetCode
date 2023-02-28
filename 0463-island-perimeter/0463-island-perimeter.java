class Solution {
    public int islandPerimeter(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int f = 0;
        for (int i = 0;i<n;i++)
        {
            for (int j = 0;j<m;j++)
            {
                if (grid[i][j] == 0)
                {
                    
                }
                else
                {
                    if (j == 0)
                    {
                        f++;
                    }
                    if (i == 0)
                    {
                        f++;
                    }
                    if (j == m-1)
                    {
                        f++;
                    }
                    if (i == n-1)
                    {
                        f++;
                    }
                    if (j > 0)
                    {
                        if (grid[i][j-1] == 0)
                        {
                            f++;
                        }
                    }
                    if (j < m-1)
                    {
                        if (grid[i][j+1] == 0)
                        {
                            f++;
                        }
                    }
                    if (i > 0)
                    {
                        if (grid[i-1][j] == 0)
                        {
                            f++;
                        }
                    }
                    if (i < n-1)
                    {
                        if (grid[i+1][j] == 0)
                        {
                            f++;
                        }
                    }
                }
            }
        }
        return f;
    }
}