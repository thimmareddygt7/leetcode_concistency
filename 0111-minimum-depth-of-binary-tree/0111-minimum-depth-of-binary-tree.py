
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if root.left is None:
            return 1 + right

        if root.right is None:
            return 1 + left

        return 1 + min(left, right)
