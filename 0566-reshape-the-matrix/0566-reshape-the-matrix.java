class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int n = mat.length;
        int m = mat[0].length;
        int[][] ne = new int[r][c];
        if (n*m != r*c)
        {
            return mat;
        }
        Deque<Integer> q = new LinkedList<Integer>();
        for (int i = 0; i<n;i++)
        {
            for (int j = 0; j<m;j++)
            {
                q.addLast(mat[i][j]);
            }
        }
        for (int i = 0;i<r;i++)
        {
            for (int j=0;j<c;j++)
            {
                ne[i][j] = q.removeFirst();
            }
        }
        return ne;
    }
}