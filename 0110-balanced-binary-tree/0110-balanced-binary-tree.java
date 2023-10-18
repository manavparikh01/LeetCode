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
    public boolean balan = true;
    
    public boolean isBalanced(TreeNode root) {
        int height = 0;
        height = isBalanc(root);
        return balan;
    }
    
    public int isBalanc(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        int lh = isBalanc(root.left);
        int rh = isBalanc(root.right);
        if (lh - rh > 1 || rh - lh > 1)
        {
            balan = false;
            return 0;
        }
        return Math.max(lh, rh) + 1;
    }
}