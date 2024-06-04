# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
            if root == [] :
                return False 
            check ,levels , q = False , [[[root]]] , deque([root])
            while q :
                n = len(q)
                temp = []
                for i in range(n) :
                    temp2 = []
                    node = q.popleft()
                    if node.left :
                        temp2.append(node.left)
                        q.append(node.left)
                    if node.right :
                        temp2.append(node.right)
                        q.append(node.right)
                    if temp2 != [] :
                        temp.append(temp2)
                if temp != [] :
                    levels.append(temp)
            n = len(levels)
            par1 , par2 , lev1 , lev2 , chk1 ,chk2= None , None , None , None ,False , False
            for i in range(n) :
                level = levels[i]
                nLev = len(level)
                for num in range(nLev) :
                    levelitems = level[num]
                    for o in levelitems :
                        if o.val == x :
                            chk1 = True
                            par1 = num
                            lev1 = i 
                        if o.val == y :
                            chk2 = True 
                            par2 = num
                            lev2 = i
                if chk1 == True and chk2 == True :
                    break 
            return par1 != par2 and lev1 == lev2
        