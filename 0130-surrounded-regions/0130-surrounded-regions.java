class Solution {
    public boolean visited[][];
    public boolean visi[][];
    
    public void solve(char[][] board) {
        int m = board.length;
        int n = board[0].length;
        visited = new boolean[m][n];
        visi = new boolean[m][n];
        for (int i = 0;i<m;i++)
        {
            if (board[i][0] == 'O')
            {
                doRoam(board, m, n, i, 0);
            }
            if (board[i][n-1] == 'O')
            {
                doRoam(board, m, n, i, n-1);
            }
        }
        for (int j = 0;j<n;j++)
        {
            if (board[0][j] == 'O')
            {
                doRoam(board, m, n, 0, j);
            }
            if (board[m-1][j] == 'O')
            {
                doRoam(board, m, n, m-1, j);
            }
        }
        for (int i = 0;i<m;i++)
        {
            for (int j = 0;j<n;j++)
            {
                if (board[i][j] == 'O' && visited[i][j] == false)
                {
                    board[i][j] = 'X';
                }
            }
        }
    }
    
    public void doRoam(char[][] board, int m, int n, int i, int j)
    {
        if (i < 0 || j < 0 || i == m || j == n || board[i][j] == 'X')
        {
            return;
        }
        if (visi[i][j] == true || visited[i][j] == true)
        {
            return;
        }
        visited[i][j] = true;
        visi[i][j] = true;
        doRoam(board, m, n, i, j+1);
        doRoam(board, m, n, i+1, j);
        doRoam(board, m, n, i, j-1);
        doRoam(board, m, n, i-1, j);
        visi[i][j] = false;
    }
}