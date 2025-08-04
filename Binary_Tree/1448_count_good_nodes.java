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
    int count = 0;

    public int goodNodes(TreeNode root) {
        DFS(root, root.val);
        return count;
    }

    public void DFS(TreeNode root, int maxVal){
        if(root.val >= maxVal){
            count += 1;
            maxVal = root.val;
        }

        if(root.left != null)
            DFS(root.left, maxVal);
        if(root.right != null)
            DFS(root.right, maxVal);
    }
}