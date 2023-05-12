class NumArray {
    public int sumArray[];
    public NumArray(int[] nums) {
        sumArray = new int[nums.length+1];
        //sumArray[0] = nums[0];
        for (int i = 0;i<nums.length;i++)
        {
            sumArray[i+1] = sumArray[i] + nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        return sumArray[right+1] - sumArray[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */