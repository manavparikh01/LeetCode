class Solution {;
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int sum = 0;
        int num = 0;
        for (int i=0;i<arr1.length;i++)
        {
            //System.out.println(arr1[i]+ "hehehhe");
            sum = 0;
            for (int j=0;j<arr2.length;j++)
            {
                if (arr1[i] - arr2[j] >= -d && arr1[i] - arr2[j] <= d)
                {
                    sum++;
                }
                //System.out.println(arr1[i] - arr2[j]);
            }
            //System.out.println(sum + "before");
            if (sum == 0)
            {
                num++;
            }
            //System.out.println(num + "before");
        }
        return num;
    }
}