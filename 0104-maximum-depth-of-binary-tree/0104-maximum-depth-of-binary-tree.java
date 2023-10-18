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
    public int maxDepth(TreeNode root) {
        int height = 1;
        return maxHeight(root, height);
    }
    
    public int maxHeight(TreeNode root, int height)
    {
        if (root == null)
        {
            return height - 1;
        }
        int lh = maxHeight(root.left, height + 1);
        int rh = maxHeight(root.right, height + 1);
        return Math.max(lh, rh);
    }
}