"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        if root == None :
            return None 
        level =[root] 
        while level :
            temp = []
            for num in range(len(level)) :
                if num != len(level) - 1 :
                    level[num].next = level[num+1]
                if level[num].left :
                    temp.append(level[num].left)
                if level[num].right :
                    temp.append(level[num].right)
            if temp != [] :
                level = temp[:]
            else :
                break
        return root
        