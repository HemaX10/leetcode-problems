# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if root == None :
            return None 
        ans ,level = [[root.val]] , [root] 
        while level :
            temp = []
            for node in level :
                if node.left :
                    temp.append(node.left)
                if node.right :
                    temp.append(node.right)
            if temp != [] :
                ans.append([x.val for x in temp])
                level = [x for x in temp]
            else :
                break
        return ans[::-1]
        