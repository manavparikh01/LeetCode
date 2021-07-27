class Solution {
    public String truncateSentence(String s, int k) {
        String su="";
        int sum=0;
        int index=0;
        for (int i=0;i<s.length();i++)
        {
            if(sum<k)
            {
                
                if (Character.isWhitespace(s.charAt(i)))
                {
                    sum++;
                    index = i;
                    
                }
            }
        }
        if (sum<k)
        {
            su=s;
            return su;
        }
        su = s.substring(0,index);
        return su;
    }
}