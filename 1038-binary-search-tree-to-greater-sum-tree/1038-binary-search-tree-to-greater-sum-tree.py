# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0  # running sum
        
        def dfs(node):
            if not node:
                return
            # Traverse right subtree first (larger values)
            dfs(node.right)
            
            # Update running sum and node value
            self.total += node.val
            node.val = self.total
            
            # Traverse left subtree
            dfs(node.left)
        
        dfs(root)
        return root