class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#In-Order
def inorder_traversal (root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

#Pre-Order
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

#Post Order
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

#Swapping Subtrees-Post Order
def swap_subtrees(root):
    if root:
        print(root.value, end=" ")
        swap_subtrees(root.right)
        swap_subtrees(root.left)

        return root

#Swapping Subtrees-In order
'''def swap_inorder(root):
    if root:
        inorder_traversal(root.right)
        print(root.value, end=" ")
        inorder_traversal(root.left)'''





root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("In-Order Traversal")
inorder_traversal(root)
print("\nPre-order Traversal")
preorder_traversal(root)
print("\nPost Order Traversal")
postorder_traversal(root)

#swap_subtrees(root)
swap_subtrees(root)
print("\n Swap In order traversal")

print("In-Order Traversal")
inorder_traversal(root)
print("\nPre-order Traversal")
preorder_traversal(root)
print("\nPost Order Traversal")
postorder_traversal(root)

