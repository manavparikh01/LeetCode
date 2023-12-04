class Solution {
    public boolean pacific[][];
    public boolean atlantic[][];
    public boolean visi[][];
    
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> l = new ArrayList<>();
        int m = heights.length;
        int n = heights[0].length;
        pacific = new boolean[m][n];
        atlantic = new boolean[m][n];
        visi = new boolean[m][n];
        for (int i = 0;i<m;i++)
        {
            findSea(heights, m, n, i, 0, heights[i][0], pacific);
            findSea(heights, m, n, i, n-1, heights[i][n-1], atlantic);
        }
        for (int j = 0;j<n;j++)
        {
            findSea(heights, m, n, 0, j, heights[0][j], pacific);
            findSea(heights, m, n, m-1, j, heights[m-1][j], atlantic);
        }
        for (int i = 0;i<m;i++)
        {
            for (int j = 0;j<n;j++)
            {
                if (pacific[i][j] == true && atlantic[i][j] == true)
                {
                    List<Integer> ll = new ArrayList<>();
                    ll.add(i);
                    ll.add(j);
                    l.add(new ArrayList<>(ll));
                }
            }
        }
        return l;
    }
    
    public void findSea(int[][] heights, int m, int n, int i, int j, int h, boolean[][] visited)
    {
        if (i < 0 || j < 0 || i == m || j == n || heights[i][j] < h)
        {
            return;
        }
        if (visi[i][j] == true)
        {
            return;
        }
        if (visited[i][j] == true)
        {
            return;
        }
        visited[i][j] = true;
        visi[i][j] = true;
        findSea(heights, m, n, i, j+1, heights[i][j], visited);
        findSea(heights, m, n, i+1, j, heights[i][j], visited);
        findSea(heights, m, n, i, j-1, heights[i][j], visited);
        findSea(heights, m, n, i-1, j, heights[i][j], visited);
        visi[i][j] = false;
        return;
    }
    
    
}