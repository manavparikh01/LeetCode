class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int num1=0;
        int j=0;
        int k=0;
        int[] arr = new int[2];
        for(int i =0;i<numbers.length;i++)
        {
            num1=numbers[i];
            j=i+1;
            int num=numbers.length-1;
            while(j<=num)
            {
                int mid = j+(num-j)/2;
                if(num1+numbers[mid]==target)
                {
                    k=mid;
                    arr[0]=i+1;
                    arr[1]=k+1;
                }
                if (num1+numbers[mid]<target)
                {
                    j=mid+1;
                } 
                else {
                    num=mid-1;
                }
            }
            
        }
        return arr;
    }
}