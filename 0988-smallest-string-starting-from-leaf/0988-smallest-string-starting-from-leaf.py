# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        lst=[]
        def path(node,curr_st):
            if not node:
                return
            curr_st+=chr(97+node.val)
            if not node.left and not node.right:
                lst.append(curr_st[::-1])
            path(node.left,curr_st)
            path(node.right,curr_st)
        path(root,"")
        return min(lst)