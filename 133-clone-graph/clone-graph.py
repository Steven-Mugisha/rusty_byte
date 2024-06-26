"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes_completed = {}

        def cloneHelper(node):
            if not node:
                return None
            
            cloned_node = Node(node.val)
            nodes_completed[node] = cloned_node

            for nei in node.neighbors:
                curr_node = nodes_completed.get(nei)
                if not curr_node:
                    cloned_node.neighbors.append(cloneHelper(nei))
                else:
                    cloned_node.neighbors.append(curr_node)
            
            return cloned_node
        
        return cloneHelper(node)
    



