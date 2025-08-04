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
    HashMap<Integer, Integer> levelNode = new HashMap<>();
    
    // The idea here is to create a hashmap that store level:most-right-node
    // we do this by DFS
    // at each level, from left to right, we keep updating the most right node
    // then at the end, we just do a for loop of the hashmap
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        if (root != null) {
            DFS(root, 0);

            for (Integer i : levelNode.values()) {
                result.add(i);
            }
        }

        return result;
    }

    public void DFS(TreeNode root, int level) {
        levelNode.put(level, root.val);

        if (root.left != null)
            DFS(root.left, level + 1);
        if (root.right != null)
            DFS(root.right, level + 1);

        return;
    }
}