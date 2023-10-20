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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> li = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        if (root == null)
        {
            return li;
        }
        q.add(root);
        while (q.size() > 0)
        {
            int size = q.size();
            for (int i = 0;i<size;i++)
            {
                TreeNode node = q.poll();
                if (i == size - 1)
                {
                    li.add(node.val);
                }
                if (node.left != null)
                {
                    q.add(node.left);
                }
                if (node.right != null)
                {
                    q.add(node.right);
                }
            }
        }
        return li;
    }
}