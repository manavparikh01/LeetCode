class Solution {
    public boolean arr[][];
    
    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int count = 0;
        arr = new boolean[n][m];
        for (int i = 0;i<n;i++)
        {
            for (int j = 0;j<m;j++)
            {
                if (grid[i][j] == '1')
                {
                    findNum(grid, i, j, n, m);
                    count++;
                }
            }
        }
        return count;
    }
    
    public void findNum(char[][] grid, int i, int j, int n, int m)
    {
        if (j == m || j<0)
        {
            return;
        }
        
        if (i == n || i<0)
        {
            return;
        }
        //System.out.println(i + " " + j + " " + grid[i][j] + " " + n + " " + m);
        if (grid[i][j] == '0')
        {
            return;
        }
        if (arr[i][j] == true)
        {
            return;
        }
        arr[i][j] = true;
        findNum(grid, i, j+1,n,m);
        findNum(grid, i+1,j,n,m);
        findNum(grid, i, j-1,n,m);
        findNum(grid, i-1,j,n,m);
        grid[i][j] = '0';
    }
}