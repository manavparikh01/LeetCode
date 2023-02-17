class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> st = new Stack<Integer>();
        int[] arr = new int[nums2.length];
        st.push(nums2[nums2.length - 1]);
        arr[nums2.length -1] = -1;
        int [] ar = new int[nums1.length];
        for (int i = nums2.length-2;i>=0;i--)
        {
            while (st.isEmpty() == false && nums2[i] >= st.peek())
            {
                st.pop();
            }
            int next = (st.isEmpty() == true)?(-1):(st.peek());
            arr[i] = next;
            st.push(nums2[i]);
        }
        for (int i=0;i<nums1.length;i++)
        {
            for (int j=0;j<nums2.length;j++)
            {
                if (nums1[i] == nums2[j])
                {
                    ar[i] = arr[j];
                }
            }
        }
        return ar;
    }
}