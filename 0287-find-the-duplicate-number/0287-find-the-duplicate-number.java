class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        do
        {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        int slow1 = 0;
        do
        {
            slow = nums[slow];
            slow1 = nums[slow1];
        } while (slow != slow1);
        return slow;
    }
}