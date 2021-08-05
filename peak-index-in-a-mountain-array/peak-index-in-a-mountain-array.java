class Solution {
    public int peakIndexInMountainArray(int[] arr) {
//         int max=0;
//         int i =0;
//         int j = arr.length -1;
//         while (i <= j)
//         {
//             int m = i + (j -i)/2;
//             if (arr[m] > arr[m-1] && arr[m] > arr[m+1])
//             {
//                 max = m;
//                 return max;
//             }
            
//             if (arr[m] < arr[m-1])
//             {
//                 j = m - 1;
//             }
//             else 
//             {
//                 i = m + 1;
//             }
//         }
//         return max;
        int i =0;
        while (arr[i] < arr[i+1])
        {
            i++;
        }
        return i;
    }
}