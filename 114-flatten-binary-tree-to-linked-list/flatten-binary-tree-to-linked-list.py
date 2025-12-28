class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)

        # Store the right subtree
        temp = root.right

        # Move left subtree to the right
        root.right = root.left
        root.left = None

        # Find the end of the new right subtree
        current = root
        while current.right:
            current = current.right

        # Attach the original right subtree
        current.right = temp
