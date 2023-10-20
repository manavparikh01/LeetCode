/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public boolean findOne = false;
    public boolean findTwo = false;
    public TreeNode sa;
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (p.val > q.val)
        {
            TreeNode temp = p;
            p = q;
            q = temp;
        }
        findLow(root, p, q);
        return sa;
    }
    
    public void findLow(TreeNode root, TreeNode p, TreeNode q)
    {
        if (root != null && sa == null)
        {
            if (root.val >= p.val && root.val <= q.val)
            {
                sa = root;
            }
            if (root.val > p.val && root.val > q.val)
            {
                findLow(root.left, p, q);
            }
            else
            {
                findLow(root.right, p, q);
            }
        }
    }
        
}