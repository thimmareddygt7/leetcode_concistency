class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        # If it's a leaf node, depth is 1
        if root.left is None and root.right is None:
            return 1
            
        # If left child is missing, only traverse right side
        if root.left is None:
            return 1 + self.minDepth(root.right)
            
        # If right child is missing, only traverse left side
        if root.right is None:
            return 1 + self.minDepth(root.left)
            
        # If both exist, find the minimum of both
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
