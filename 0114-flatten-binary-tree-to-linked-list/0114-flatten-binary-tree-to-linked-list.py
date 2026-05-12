# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
            curr=root
            while curr:
                if curr.left:
                    fast=curr.left
                    while fast.right:
                        fast=fast.right
                    fast.right=curr.right
                    curr.right=curr.left
                    curr.left=None
                curr=curr.right
#------------------------------------------------------------------------------
    # def __init__(self):
    #     self.stack=[]
    # def flatten(self, root):
    #     # if root.right:
    #     #     self.stack.append(root.right)
    #     #     root.right=None
    #     # if root.left:
    #     #     self.stack.append(root.left)
    #     #     root.left=None
        
    #     # root.right=st 


#--------------------------------------------------------------------------------
    # def __init__(self):
    #     self.prev=None
    # def flatten(self, root):
    #     if not root:
    #         return None
    #     self.flatten(root.right)
    #     self.flatten(root.left)

    #     root.right=self.prev
    #     root.left=None

    # """
    # :type root: Optional[TreeNode]
    # :rtype: None Do not return anything, modify root in-place instead.
    # """
        
        