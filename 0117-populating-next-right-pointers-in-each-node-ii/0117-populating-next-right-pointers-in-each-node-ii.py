"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        parent=root
        dummy=Node()
        while parent:
            curr=parent
            child=dummy
            while curr:
                if curr.left:
                    child.next=curr.left
                    child=child.next
                if curr.right:
                    child.next=curr.right
                    child=child.next
                curr=curr.next
            parent=dummy.next
            dummy.next=None
        return root




        # curr=root
        # dummy=Node()
        # # while parent:
        # #     curr=parent
        # child=dummy
        # while curr:
        #     if curr.left:
        #         child.next=curr.left
        #         child=child.next
        #     if curr.right:
        #         child.next=curr.right
        #         child=child.next
        #     curr=curr.next
        # curr=dummy.next
        # dummy.next=None
        # return root








        # if not root:
        #     return None
        # else:
        #     # if root.left is not None:
        #     if root.left:
        #         root.left.next=root.right
        #         # if root.right is not None and root.next is not None:
        #         if root.right and root.next:
        #             root.right.next=root.next.left
        #     elif root.right:
        #         root.right.next=root.next
        #         # if root.
        # self.connect(root.left)
        # self.connect(root.right)
        # return root






        # if not root:
        #     return None
        # else:
        #     if root.
