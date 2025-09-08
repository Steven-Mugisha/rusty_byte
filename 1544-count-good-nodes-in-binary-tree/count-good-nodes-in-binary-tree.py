# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # return value:
        # need to return the count of good nodes in each subtree
            # this means for each node I need to know the good nodes from the left and right children. (recurse will hadndle this)
        
        # state: pass the maximum so far

        def dfs(node, maxSoFar):
            if not node:
                return 0
            
            total = 0

            if node.val >= maxSoFar:
                total += 1
                
            total += dfs(node.left, max(maxSoFar, node.val))
            total += dfs(node.right, max(maxSoFar, node.val))

            return total
    
        from math import inf
    
        return dfs(root, -inf)

