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
    public int sum;
    public Stack<TreeNode> st;
    
    public int goodNodes(TreeNode root) {
        st = new Stack<TreeNode>();
        parseTree(root, st);
        return sum;
    }
    
    public void parseTree(TreeNode root, Stack<TreeNode> st)
    {
        if (root == null)
        {
            return;
        }
        if (st.size() != 0)
        {
            if (root.val >= st.peek().val)
            {
                st.push(root);
                sum++;
            }
            
        }
        else
        {
            st.push(root);
            sum++;
        }
        parseTree(root.left, st);
        parseTree(root.right, st);
        if (root == st.peek())
        {
            st.pop();
        }
    }
}