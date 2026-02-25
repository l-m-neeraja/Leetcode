# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        lst=[]
        def path(node,curr):
            if not node:
                return
            curr+=node.val
            if not node.left and not node.right:
                lst.append(curr)
                return
            path(node.left,curr)
            path(node.right,curr)
        path(root,0)
        if targetSum in lst:
            return True
        return False