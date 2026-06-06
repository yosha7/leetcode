# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if self.isSame(root,subRoot):
            return True
        left=self.isSubtree(root.left,subRoot)
        right=self.isSubtree(root.right,subRoot)
        return left or right
    def isSame(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        left=self.isSame(p.left,q.left)
        right=self.isSame(p.right,q.right)
        return left and right
        
        