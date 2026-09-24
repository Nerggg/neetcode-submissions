
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def calc_depth(root: Optional[TreeNode]) -> int:
            nonlocal result
            if not root:
                return 0

            depth_left = calc_depth(root.left) if root and root.left else 0
            depth_right = calc_depth(root.right) if root and root.right else 0

            if depth_left > depth_right + 1:
                result = False
            elif depth_right > depth_left + 1:
                result = False

            return 1 + max(depth_left, depth_right)

        calc_depth(root)
        # print("depth_left:", depth_left)
        # print("depth_right:", depth_right)

        return result
        
