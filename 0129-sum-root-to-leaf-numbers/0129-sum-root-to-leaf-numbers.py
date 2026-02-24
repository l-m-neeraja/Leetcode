# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        lst=[]
        def path(node,curr):
            if not node:
                return
            curr+=str(node.val)
            if not node.left and not node.right:
                lst.append(curr)
            path(node.left,curr)
            path(node.right,curr)
        path(root,"")
        res=0
        for i in lst:
            res+=int(i)
        return res
