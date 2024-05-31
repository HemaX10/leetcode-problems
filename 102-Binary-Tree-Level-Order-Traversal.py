# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root == None :
            return []
        elif root.right == None and root.left == None :
            return [[root.val]]
        else :
            queue , level , taken = [root] , [[root]] ,[] 
            while queue :
                node = queue.pop(0)
                queue.extend(filter(None , [node.left ,node.right]))
                if len(level) -1 not in taken:
                    taken.append(len(level) -1)
                    test = []
                    for x in level[-1] :
                        test.extend(filter(None , [x.left ,x.right]))
                    if test != [] :
                        level.append(test)
            returnable = []
            for li in level :
                needed = []
                for obj in li :
                    needed.append(obj.val)
                returnable.append(needed)
            return returnable
        