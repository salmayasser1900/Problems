# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        res, stack = [], []
        
        while(root!=None or stack != None):
            
            while(root!=None):
                stack.append(root)
                res.append(root.val)
                root = root.left
        
            if not stack:
                return res
            
            node = stack.pop()
            root = node.right
        
        return res