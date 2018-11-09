# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use recurisive to solve tree problem 
#if the tree is null they are equal
#if the parents node are equal then judge wehther their left and right node are equal
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
      
        if not p and not q:
                return True
        if not p or not q:
                return False
        if p.val==q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
            