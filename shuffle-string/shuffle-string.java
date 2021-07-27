class Solution {
    public String restoreString(String s, int[] indices) {
        String su = "";
        char[] arr = new char[indices.length+1];
        for (int i=0;i<indices.length;i++)
        {
            arr[indices[i]] = s.charAt(i);
        }
        for (int i=0; i<indices.length;i++)
        {
            su = su + arr[i];
        }
        return su;
    }
}