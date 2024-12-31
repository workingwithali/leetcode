# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        res = []
        q = collections.deque([root])
        while q:
            rightside = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightside =node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)

        return res