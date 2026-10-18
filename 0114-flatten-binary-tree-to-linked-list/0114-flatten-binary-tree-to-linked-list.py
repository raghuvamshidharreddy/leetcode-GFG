class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        if not root:
            return

        s = []

        def preorder(node):
            if not node:
                return
            s.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(s) - 1):
            s[i].left = None
            s[i].right = s[i + 1]

        s[-1].left = None
        s[-1].right = None
