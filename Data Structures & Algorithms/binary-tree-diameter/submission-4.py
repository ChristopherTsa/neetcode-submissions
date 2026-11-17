class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        heights = {}
        max_diameter = 0
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if not node:
                continue

            if visited:
                left_h = heights.get(node.left, 0)
                right_h = heights.get(node.right, 0)
                max_diameter = max(max_diameter, left_h + right_h)
                heights[node] = 1 + max(left_h, right_h)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return max_diameter
