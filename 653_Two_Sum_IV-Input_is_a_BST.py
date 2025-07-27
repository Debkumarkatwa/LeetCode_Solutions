class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    def inorder(node, seen):
        if not node:
            return False
        if k - node.val in seen:
            return True
        seen.add(node.val)
        return inorder(node.left, seen) or inorder(node.right, seen)
    return inorder(root, set())

# Example usage:
# Construct the tree: [5,3,6,2,4,null,7]
root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(6, None, TreeNode(7))

k = 9
print(findTarget(root, k))  # Output: True