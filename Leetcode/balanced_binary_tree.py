from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:

    def is_balanced(self, root: 'TreeNode'):

        if root is None:
            return True

        lh = self.get_height(root.left)
        rh = self.get_height(root.right)

        balanced = abs(lh - rh) < 2
        left_balanced = self.is_balanced(root.left)
        right_balanced = self.is_balanced(root.rigth)
        
        return balanced and left_balanced and right_balanced

    


    def get_height(self, root: 'TreeNode') -> int:

        if root is None:
            return 0

        return max(self.get_height(root.left), self.get_height(root.right)) + 1