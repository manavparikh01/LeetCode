class Solution {
    public int[][] side;
    public int c, r;
    
    public boolean exist(char[][] board, String word) {
        side = new int[board.length][board[0].length];
        r = board.length;
        c = board[0].length;
        for (int i = 0;i<r;i++)
        {
            for (int j = 0;j<c;j++)
            {
                if (doesExist(board, word, 0, i, j) == true)
                {
                    return true;
                }
            }
        }
        return false;
    }
    
    public boolean doesExist(char[][] board, String word, int wordCount, int rc, int cc)
    {
        if (isSafe(rc, cc) == false || wordCount == word.length() || board[rc][cc] != word.charAt(wordCount))
        {
            return false;
        }
        if (board[rc][cc] == word.charAt(wordCount) && wordCount == word.length() - 1)
        {
            return true;
        }
        
        side[rc][cc] = 1;
        boolean exists = doesExist(board, word, wordCount+1, rc+1, cc) || doesExist(board, word, wordCount+1, rc, cc+1) || doesExist(board, word, wordCount+1, rc-1, cc) || doesExist(board, word, wordCount+1, rc, cc-1);
        
        side[rc][cc] = 0;
                
        return exists;
    }
    
    public boolean isSafe(int rc, int cc)
    {
        return (rc > -1 & rc < r && cc > -1 && cc < c && side[rc][cc] == 0);
    }
}