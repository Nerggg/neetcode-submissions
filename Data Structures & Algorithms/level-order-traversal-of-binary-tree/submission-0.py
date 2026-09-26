
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []

        while queue:
            temp = []
            for i in range (len(queue)):
                node = queue.popleft()
                if not node: continue
                temp.append(node.val)
                
                queue.append(node.left)
                queue.append(node.right)

            if len(temp) > 0: result.append(temp)

        return result

