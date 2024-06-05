# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self) :
        self.diamater = 0 
    def diameterOfBinaryTree(self, root):
        self.height(root)
        return self.diamater - 1
    def height(self , node) :
        if node == None :
            return 0
        else :
            leftHeight = self.height(node.left)
            rigthHeight = self.height(node.right)

            dia = leftHeight + rigthHeight + 1
            self.diamater = max(self.diamater , dia)
            return max(leftHeight , rigthHeight) + 1
        