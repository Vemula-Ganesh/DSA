# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
         self.c = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root:
            self.countNodes(root.left)
            self.c+=1
            self.countNodes(root.right)
        return self.c
        