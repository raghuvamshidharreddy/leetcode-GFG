# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, current, res):
            if not node:
                return
            current += str(node.val)
            if not node.left and not node.right:  # leaf node
                res.append(int(current))
                return
            helper(node.left, current, res)
            helper(node.right, current, res)

        res = []
        helper(root, '', res)
        return sum(res)