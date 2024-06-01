# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        ans , level = [] , [root]
        while level : 
            result = 0.0
            temp = []
            for x in level :
                result += float(x.val) 
                if x.left :
                    temp.append(x.left)
                if x.right :
                    temp.append(x.right)
            result = result / float(len(level))
            ans.append(result)
            level = [x for x in temp]
        return ans
        