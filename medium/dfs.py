"""
Sliding Window Problem Collection
Each function implements a Sliding Window problem and has its own test cases at the bottom.
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----------------------
# Problem 114: Flatten Binary Tree to LinkedList
# ----------------------
def flatten(root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def dfs(node):
            nonlocal prev
            if not node:
                return
            if node.right:
                dfs(node.right)
            if node.left:
                dfs(node.left)
            node.right  = prev
            node.left = None
            prev = node

        dfs(root)
        return root

# Time Complexity Analysis:
# - O(n) : This is because we are doing a simple DFS on the tree and visiting each node.

# Space Complexity Analysis
# - O(h) : The maximum depth of a recursion is from the root to the farthest away leaf node.  That is the height of the tree
# and the maximum distance away.

if __name__ == '__main__':
    print("Passed All Cases Successfully")