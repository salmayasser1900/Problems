
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            ans = abs(self.depth(root.left)-self.depth(root.right))
            if ans <= 1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False
             
    def depth(self,root):
        if not root or root.val == None:
            return 0
        else:
            return max(self.depth(root.left),self.depth(root.right))+1