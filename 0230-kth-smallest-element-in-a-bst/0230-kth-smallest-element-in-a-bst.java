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
    public int h = 0;
    public TreeNode node;
    
    public int kthSmallest(TreeNode root, int k) {
        findKth(root, k);
        return node.val;
    }
    
    public void findKth(TreeNode root, Integer k)
    {
        if (root != null && h < k)
        {
            findKth(root.left, k);
            h++;
            //System.out.println(root.val + " " + h);
            if (h == k)
            {
                node = root;
            }
            findKth(root.right, k);
        }
        
    }
}