# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        """Approch1"""
        # res=[]
        # def add(i,tree):
        #     if len(res)<=i:
        #         res.append([tree.val])
        #     else:
        #         res[i].append(tree.val)
        #     i+=1
        #     if tree.left:
        #         add(i,tree.left)
        #     if tree.right:
        #         add(i,tree.right)
        # if root:
        #     add(0,root)
        # for i in range(len(res)):
        #     if i%2!=0:
        #         res[i].reverse()
        # return res

        
        """Approch 2"""
        res=[]
        def add(i,tree):
            if len(res)<=i:
                res.append([tree.val])
            elif i%2==0:
                res[i].append(tree.val)
            elif i%2!=0:
                res[i].insert(0,tree.val) 
            i+=1
            if tree.left:
                add(i,tree.left)
            if tree.right:
                add(i,tree.right)
        if root:
            add(0,root)
        return res

        

        