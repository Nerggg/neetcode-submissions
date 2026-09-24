
class Solution:
    def __maxDepthHelper(self, root: Optional[TreeNode], result: int) -> int:
        if not root:
            return result

        result += 1
        result_from_left = self.__maxDepthHelper(root.left, result) if root.left else 0
        result_from_right = self.__maxDepthHelper(root.right, result) if root.right else 0

        return max(result_from_left, result_from_right, result)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.__maxDepthHelper(root, 0)

