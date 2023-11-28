class Solution {
    public List<List<String>> l;
    public List<String> ll;
    public boolean arr[][];
    
    public List<List<String>> solveNQueens(int n) {
        l = new ArrayList<>();
        ll = new ArrayList<>();
        arr = new boolean[n][n];
        if (n == 1)
        {
            ll.add("Q");
            l.add(new ArrayList<>(ll));
            return l;
        }
        
        nQueens(n, 0);
        
        
        return l;
    }
    
    public void nQueens(int n, int r)
    {
        if (r == n)
        {
            List<String> lll = new ArrayList<>();
            for (int i = 0;i<n;i++)
            {
                String s = "";
                for (int j = 0;j<n;j++)
                {
                    if (arr[i][j])
                    {
                        s = s + 'Q';
                    }
                    else
                    {
                        s = s + '.';
                    }
                }
                lll.add(s); 
            }
            l.add(new ArrayList<>(lll));
            return;
        }
        
        for (int j = 0;j<n;j++)
        {
            if (isSafe(r, j, n) == true)
            {
                arr[r][j] = true;
                r++;
                nQueens(n, r);
                
                r--;
                arr[r][j] = false;
            }
        }
        
        return;
    }
    
    public boolean isSafe(int i, int j, int n)
    {
        for (int a = 0; a<n;a++)
        {
            if (arr[i][a] == true)
            {
                return false;
            }
        }
        
        for (int b = 0; b<n;b++)
        {
            if (arr[b][j] == true)
            {
                return false;
            }
        }
        
        for (int a = i,b = j; a>= 0 && b>=0;a--,b--)
        {
            if (arr[a][b] == true)
            {
                return false;
            }
        }
        
        for (int a = i, b = j; a>=0 && b<n;a--,b++)
        {
            if (arr[a][b] == true)
            {
                return false;
            }
        }
        
        return true;
    }
}