/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0
    let h = nums.length - 1
    while (l <= h)
    {
        let mid = Math.floor((l + h) / 2)
        if (nums[mid] === target)
        {
            return mid
        }
        else if (nums[mid] > target)
        {
            h = mid - 1
        }
        else
        {
            l = mid + 1
        }
    }
    return -1
};