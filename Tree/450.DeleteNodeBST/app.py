class TreeNode:
    def __init__(self,val= 0 ,right = None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution :
    def delete(self,root,key):
        if not root:
            return None
        if key > root.val:
            root.right = self.delete(root.right,key)
        elif key< root.val:
            root.left = self.delete(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            

