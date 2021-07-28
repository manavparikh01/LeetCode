class Solution {
    public int largestAltitude(int[] gain) {
        int[] arr = new int[gain.length+1];
        arr[0]=0;
        int net=0;
        int max=0;
        for (int i=0;i<gain.length;i++)
        {
            net= arr[i]+gain[i];
            arr[i+1]=net;
            //System.out.println(arr[i+1]);
            if(net>max)
            {
                max=net;
            }
        }
        return max;
    }
}