class Solution {
    public void setZeroes(int[][] matrix) {
        int l = matrix.length;
        int b = matrix[0].length;
        HashSet<Integer> hml = new HashSet<>();
        HashSet<Integer> hmb = new HashSet<>();
        boolean[][] mat = new boolean[l][b];
        // for (int i = 0;i<l;i++)
        // {
        //     for (int j = 0;j<b;j++)
        //     {
        //         mat[i][j] = 
        //     }
        // }
        for (int i = 0;i<l;i++)
        {
            for (int j = 0;j<b;j++)
            {
                if (mat[i][j] == true)
                {
                    continue;
                }
                if (matrix[i][j] == 0)
                {
                    hml.add(i);
                    hmb.add(j);
                    for (int m = 0;m<b;m++)
                    {
                        if (matrix[i][m] == 0)
                        {
                            continue;
                        }
                        matrix[i][m] = 0;
                        mat[i][m] = true;
                    }
                    for (int n = 0;n<l;n++)
                    {
                        if (matrix[n][j] == 0)
                        {
                            continue;
                        }
                        matrix[n][j] = 0;
                        mat[n][j] = true;
                    }
                }
            }
        }
        
        // for (int i = 0;i<l;i++)
        // {
        //     for (int j = 0;j<b;j++)
        //     {
        //         System.out.print(matrix[i][j]);
        //     }
        //     System.out.println('\n');
        // }
    }
}