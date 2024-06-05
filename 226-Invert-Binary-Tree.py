# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self , root) :
        if root == None :
            return None 
        rightSide = self.invertTree(root.right)
        leftSide = self.invertTree(root.left)
        
        root.left = rightSide 
        root.right = leftSide

        return root
        