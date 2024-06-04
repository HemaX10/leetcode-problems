# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if root == None :
            return True 
        queue , temp = deque([root]) , []
        while queue :
            temp = []
            print(temp)
            n = len(queue)
            for i in range(n) :
                node = queue.popleft()
                if node.left :
                    queue.append(node.left)
                    print(node.left.val)
                    temp.append(node.left.val)
                else :
                    temp.append(-101)
                if node.right :
                    queue.append(node.right)
                    print(node.right.val)
                    temp.append(node.right.val)
                else :
                    temp.append(-101)
            num =len(temp)
            print(temp)
            if num % 2 != 0 :
                return False
            for i in range(num/2) :
                if temp[i] != temp[num - i - 1] :
                    return False
        return True
        