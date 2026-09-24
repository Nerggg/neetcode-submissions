
class Solution:
    def __invertTreeHelper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # edge case if root is None
        if not root:
            return None
        elif not root.left and not root.right:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.__invertTreeHelper(root)
        return root

