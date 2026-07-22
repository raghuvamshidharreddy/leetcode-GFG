# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorder(root,res):
            if root is None:
                return 
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
        self.res=[]
        inorder(root,self.res)
        self.count=-1
    def next(self) -> int:
        self.count+=1
        return self.res[self.count]

    def hasNext(self) -> bool:
        return self.count!=len(self.res)-1
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()