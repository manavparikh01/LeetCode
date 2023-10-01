class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        ArrayList<Integer> al = new ArrayList<Integer>();
        for (int i = 0;i<nums1.length;i++)
        {
            al.add(nums1[i]);
        }
        for (int i = 0;i<nums2.length;i++)
        {
            al.add(nums2[i]);
        }
        Collections.sort(al);
        if (al.size() % 2 == 0)
        {
            int b = al.get(al.size()/2) + al.get((al.size()-1)/2);
            double a = (double)b/2;
            return a;
        }
        return (double)al.get(al.size()/2);
    }
}