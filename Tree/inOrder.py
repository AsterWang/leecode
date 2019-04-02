'''
In a preorder traversal, we recursively do a inOrder traversal of the left subtree, 
then root, 
followed by a recursive inOrder traversal of the right subtree.
　　　　　　　　　　　　　　　　1

　　　　　　　　　　　　　　　/　  \

　　　　　　　　　　　　　　 2　　  3

　　　　　　　　　　　　　  /   \　 /   \

   　　　　　　　　　　　　4     5  6    7
{1} -> {1, 2} -> {1,2,4} -> {1, 2} -> {1} -> {1, 5} -> {1} -> {} -> {3} -> {3, 6} -> {3} -> {} -> {7} -> {}
result = 4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inOrder_recursive(root):
	if root:
		inOrder_recursive(root.left)
		print(root.val)
		inOrder_recursive(root.right)

def inOrder(root):
	if not root:
		return None
	stack = []
	res = []
	while stack or root:
		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			res.append(root.val)
			root = root.right
	print(res)

def inOrder(root):
	if not root:
		return None
	stack = []
	res = []
	while stack or root:
		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			res.append(root.val)
			root = root.right



t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
inOrder(t1)
print()
preOrder(t1)
print()
postOrder(t1)
