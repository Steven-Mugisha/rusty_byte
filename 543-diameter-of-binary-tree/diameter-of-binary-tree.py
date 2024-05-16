# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameterHelper(node, diameter):
            if not node:
                return 0, diameter
            else:
                lh, diameter = diameterHelper(node.left, diameter)
                rh, diameter = diameterHelper(node.right, diameter)

                diameter = max(diameter, lh+rh)
                return max(lh, rh) + 1, diameter
        
        diameter = 0
        _, diameter = diameterHelper(root, diameter)

        return diameter