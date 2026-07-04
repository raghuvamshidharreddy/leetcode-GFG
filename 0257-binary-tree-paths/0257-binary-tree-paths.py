# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def path(root,res,s):
            if root is None:
                return
            s.append(str(root.val))
            if not root.left and not root.right:
                res.add('->'.join(s))
            else:
                path(root.left,res,s)
                path(root.right,res,s)
            s.pop()
        res=set()
        s=[]
        path(root,res,s)
        return list(res)

