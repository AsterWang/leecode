'''
In a preorder traversal, we visit the root node first, 
then recursively do a preorder traversal of the left subtree, 
followed by a recursive preorder traversal of the right subtree.
　　　　　　　　　　　　　　　　　　　　　  1
　　　　　　　　　　　　　　　　　　　　　/   \

　　　　　　　　　　　　　　　　　　　　2       3

　　　　　　　　　　　　　　　　　　　/    \   /    \

　　　　　　　　　　　　　　　　　　 4       5  6     7 
{1} -> {1, 2} -> {1,2,4} -> {1, 2} -> {1} -> {1, 5} -> {1} -> {} -> {3} -> {3, 6} -> {3} -> {} -> {7} -> {}
result = 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preOrder_recursive(root):
	if root:
		print(root.val, end = " ")
		preOrder_recursive(root.left)
		preOrder_recursive(root.right)


def preOrder(root):
	stack = []
	while root or stack:
		if root:
			print(root.val, end = ' ')
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			root = root.right

def inOrder(root):
	stack = []
	while stack or root:
		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			print(root.val, end = ' ')
			root = root.right

def postOrder(root):
	stack = []
	pre = None
	if root:
		stack.append(root)
		while stack:
			curr = stack[-1]
			if (not curr.left and not curr.right) or (pre and pre == curr.left or pre == curr.right):
				print(curr.val, end = ' ')
				stack.pop()
				pre = curr
			else:
				if curr.right: stack.append(curr.right)
				if curr.left:  stack.append(curr.left)

def postOrder(root):
	stack = []
	pre = None
	if root:
		stack.append(root)
		while stack:
			curr = stack[-1]
			if (not curr.left and not curr.right) or (pre and pre == curr.left or pre == curr.right):
				stack.append(curr.val)
				stack.pop()
				pre = curr
			else:
				if curr.right: stack.append(curr.right)
				if curr.left : stack.append(curr.left)
	print(stack)


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

# preOrder_recursive(t1)
# print()
preOrder(t1)
print()
inOrder(t1)
print()
postOrder(t1)