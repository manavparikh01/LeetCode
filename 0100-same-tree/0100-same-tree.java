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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null)
        {
            return true;
        }
        if (p == null && q != null)
        {
            return false;
        }
        if (p != null && q == null)
        {
            return false;
        }
        //boolean l = isSameTree(p.left, q.left);
        if (isSameTree(p.left, q.left) == false)
        {
            return false;
        }
        //boolean r = isSameTree(p.right, q.right);
        if (isSameTree(p.right, q.right) == false)
        {
            return false;
        }
        return (p.val == q.val);
    }
}