# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.pathsum=float('-inf')
        def adder(root):
            if not root:
                return 0
            left=max(adder(root.left),0)
            right=max(adder(root.right),0)
            self.pathsum=max(self.pathsum,root.val+left+right) 
            return root.val + max(left, right)
        adder(root)

        return self.pathsum