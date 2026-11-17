class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0  # (hauteur, diamètre)
            
            left_h, left_d = dfs(node.left)
            right_h, right_d = dfs(node.right)
            
            height = 1 + max(left_h, right_h)
            diameter = max(left_h + right_h, left_d, right_d)
            return height, diameter

        return dfs(root)[1]
