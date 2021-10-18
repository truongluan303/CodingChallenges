class TreeNode:
    def __inti__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


    
class Solution:

    def min_depth(self, root: 'TreeNode'):

        if root is None:
            return 0

        if root.left is None and root.right is not None:
            return self.min_depth(root.right) + 1 

        if root.right is None and root.left is not None:
            return self.min_depth(root.left) + 1

        else:
            return min(self.min_depth(root.right), self.min_depth(root.left)) + 1