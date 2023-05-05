class Solution {
    public int[] replaceElements(int[] arr) {
        int i = -1;
        i = arr[arr.length-1];
        arr[arr.length-1] = -1;
        for (int j = arr.length-2;j>=0;j--)
        {
            int m = arr[j];
            arr[j] = i;
            i = Math.max(i,m);
        }
        return arr;
    }
}