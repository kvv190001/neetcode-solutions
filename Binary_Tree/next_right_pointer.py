#Leetcode 116: Populating Next Right Pointers in Each Node

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

def setPointer(curNode, nextNode):
    if curNode.left == None:
        return
    if nextNode == None:
        curNode.left.next = curNode.right
        setPointer(curNode.right, None)
        setPointer(curNode.left, curNode.right)
    else:
        curNode.left.next = curNode.right
        curNode.right.next = nextNode.left
        setPointer(curNode.left, curNode.right)
        setPointer(curNode.right, nextNode.left)
    return

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return root

        setPointer(root, None)
        return root

    