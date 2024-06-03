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
        q = deque([root])
        while q :
            n = len(q)
            for _ in range(n) :
                node = q.popleft()
                if _ < n -1 :
                    node.next = q[0]
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
        return root
        