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
    public boolean is = false;

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root != null && is == false)
        {
            //System.out.println(root.val + " " + subRoot.val);
            if (root.val == subRoot.val)
            {
                boolean m = parseSmall(root, subRoot);
                //System.out.println(m + " val");
                if (m == true)
                {
                    is = true;
                }
            }
            isSubtree(root.left, subRoot);
            isSubtree(root.right, subRoot);
        }
        return is;
    }

    // public void parseBig(TreeNode root, TreeNode subRoot)
    // {
    //     if (root == null)
    //     {
    //         return;
    //     }
    //     if (root.val == subRoot.val)
    //     {
    //         boolean m = parseSmall(root, subRoot);
    //         if (m == true)
    //         {
    //             //is = true
    //             return;
    //         }
    //     }
    // }

    public boolean parseSmall(TreeNode root, TreeNode subRoot)
    {
        if (root == null && subRoot == null)
        {
            return true;
        }
        if (root != null && subRoot == null)
        {
            return false;
        }
        if (root == null && subRoot != null)
        {
            return false;
        }
        boolean l = parseSmall(root.left, subRoot.left);
        if (l == false)
        {
            return false;
        }
        boolean r = parseSmall(root.right, subRoot.right);
        if (r == false)
        {
            return false;
        }
        return (root.val == subRoot.val);
    }
}