/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int max = Integer.MIN_VALUE;
    public int lh = 0;
    public int rh = 0;
    public int maxPathSum(TreeNode root) {
        maxSum(root);
        return max;
    }
    public int maxSum(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        int lh = maxSum(root.left);
        int rh = maxSum(root.right);
        int sum = lh + rh + root.val;
        int sum1 = lh + root.val;
        int sum2 = rh + root.val;
        if (sum1 > sum || sum2 > sum)
        {
            sum = Math.max(sum1, sum2);
        }
        if (root.val > sum)
        {
            sum = root.val;
        }
        max = Math.max(sum, max);
        return Math.max(root.val,Math.max(lh + root.val, rh + root.val));
    }
}