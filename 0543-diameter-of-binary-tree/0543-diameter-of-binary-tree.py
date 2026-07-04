# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameterRec(root,res):
            if root is None :
                return 0
            lh=diameterRec(root.left,res)
            rh=diameterRec(root.right,res)
            res[0]=max(res[0],lh+rh)
            return 1+max(lh,rh)
        res=[0]
        diameterRec(root,res)
        return res[0]