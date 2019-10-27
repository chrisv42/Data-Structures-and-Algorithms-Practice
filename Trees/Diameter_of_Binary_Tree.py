class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        def height(node: TreeNode):
            if not node: return 0
            L = height(node.left)
            R = height(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L,R)+1
    
        height(root)
        return self.ans-1
