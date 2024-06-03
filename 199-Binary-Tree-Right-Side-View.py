# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root == None :
            return []
        ans , level = [] , [root]
        while level :
            temp = []
            n = len(level)
            for i in range(n) :
                if i == n - 1 :
                    ans.append(level[i].val)
                if level[i].left :
                    temp.append(level[i].left)
                if level[i].right :
                    temp.append(level[i].right)
            level = temp[:]    
        return ans
        