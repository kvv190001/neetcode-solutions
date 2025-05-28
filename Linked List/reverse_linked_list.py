# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseNode(head, prevNode):
    if head.next == None:
        head.next = prevNode
        return head
    
    k = reverseNode(head.next, head)
    head.next = prevNode
    return k 

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        return reverseNode(head, None)


        