class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# In-Order
def inorder_traversal(root):
    if root:
        inorder_traversal(root.right)
        print(root.value, end=" ")
        inorder_traversal(root.left)

# Pre-Order
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Post Order
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Swapping Subtrees
def swap_subtrees(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    swap_subtrees(root.right)
    swap_subtrees(root.left)

    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("In-Order Traversal")
inorder_traversal(root)
print("\nPre-Order Traversal")
preorder_traversal(root)
print("\nPost Order Traversal")
postorder_traversal(root)

swap = swap_subtrees(root)
print("\n")
print ("After Swapping")

print("\nIn-Order Swap Traversal")
inorder_traversal(root)
print("\nPost-order Swap Traversal")
preorder_traversal(root)
print("\nPre-Order Swap Traversal")
postorder_traversal(root)
