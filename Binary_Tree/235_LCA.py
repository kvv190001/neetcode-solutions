# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            temp = q
            q = p
            p = temp

        if p.val <= root.val and q.val >= root.val:
            return root
        
        curNode = root
        if p.val < root.val:
            curNode = root.left
        else:
            curNode = root.right
            
        while True:
            print(curNode.val)
            if p.val <= curNode.val and q.val >= curNode.val:
                return curNode
            if p.val == curNode.val or q.val == curNode.val:
                return curNode
            if p.val < curNode.val and q.val < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right

        return curNode

        