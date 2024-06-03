# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root == None :
            return []
        ans , level ,counter = [[root.val]] , [root] , 0
        while level :
            temp = []
            for node in level :
                if node.right != None and node.left != None :
                    temp.extend([node.left.val ,node.right.val])
                elif node.left != None :
                    temp.append(node.left.val)
                elif node.right != None :
                    temp.append(node.right.val)
            if counter % 2 == 0 :
                if temp != [] :
                    ans.append(temp[::-1])
            else :
                if temp != [] :
                    ans.append(temp)
            counter+=1 
            temp = []
            for x in level :
                if x != None :
                    temp.extend([x.left , x.right])
            level = [x for x in temp if x]            
        return ans
        