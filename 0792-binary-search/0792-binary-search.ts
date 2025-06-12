function search(nums: number[], target: number): number {
    let l: number = 0;
    let h: number = nums.length - 1;
    while (l <= h)
    {
        let mid: number = Math.floor((l + h)/2);
        console.log(mid)
        if (nums[mid] == target)
        {
            return mid;
        }
        else if (nums[mid] > target)
        {
            h = mid - 1;
        }
        else
        {
            l = mid + 1;
        }
    }
    return -1;
};