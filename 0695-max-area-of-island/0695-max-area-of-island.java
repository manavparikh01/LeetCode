class Solution {
    public int max;
    public int count;
    public boolean arr[][];
    
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        arr = new boolean[m][n];
        for (int i = 0;i<m;i++)
        {
            for (int j = 0;j<n;j++)
            {
                if (grid[i][j] == 1)
                {
                    count = 0;
                    doSomething(grid, m, n, i, j);
                    max = Math.max(max, count);
                }
            }
        }
        return max;
    }
    
    public void doSomething(int[][] grid, int m, int n, int i, int j)
    {
        if (i < 0 || i == m || j < 0 || j == n)
        {
            return;
        }
        if (grid[i][j] == 0)
        {
            return;
        }
        if (arr[i][j] == true)
        {
            return;
        }
        arr[i][j] = true;
        count++;
        doSomething(grid, m, n, i, j+1);
        doSomething(grid, m, n, i+1, j);
        doSomething(grid, m, n, i, j-1);
        doSomething(grid, m, n, i-1, j);
        grid[i][j] = 0;
        return;
    }
}