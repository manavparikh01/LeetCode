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
    public int dia;
    
    public int diameterOfBinaryTree(TreeNode root) {
        int height = 0;
        height = diaTree(root);
        return dia;
    }
    
    public int diaTree(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        int lh = diaTree(root.left);
        int rh = diaTree(root.right);
        dia = Math.max(dia, lh + rh);
        return Math.max(lh, rh) + 1;
    }
}