# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def DFS(self, root, level, treeDict):
        if level not in treeDict:
            treeDict[level] = []
        treeDict[level].append(root.val)
        if root.left != None:
            self.DFS(root.left, level + 1, treeDict)
        if root.right != None:
            self.DFS(root.right, level + 1, treeDict)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        treeDict = {}

        if root == None:
            return []

        self.DFS(root,0,treeDict)

        result = []

        for value in treeDict.values():
            result.append(value)

        return result

