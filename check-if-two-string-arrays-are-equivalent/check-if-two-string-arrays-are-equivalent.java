class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String wordone="a";
        String wordtwo="a";
        for (int i=0;i<word1.length;i++)
        {
            wordone+=word1[i];
        }
        for (int i=0;i<word2.length;i++)
        {
            wordtwo+=word2[i];
        }
        if (wordone.equals(wordtwo))
        {
            return true;
        }
        return false;
    }
}