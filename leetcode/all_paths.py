# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        return_arr = []
        if not root: 
            return return_arr
        result= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.left)]
        result+= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.right)]
        if not result:
            return str[(root.val)]
        return result 