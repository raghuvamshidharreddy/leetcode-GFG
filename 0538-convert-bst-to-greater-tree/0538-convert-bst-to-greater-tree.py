# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root,res):
            if root is None:
                return 
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
        res=[]
        inorder(root,res)

        def changer(root,res):
            if root is None:
                return 
            idx=res.index(root.val)
            root.val=sum(res[idx:])
            changer(root.left,res)
            changer(root.right,res)
        changer(root,res)
        return root