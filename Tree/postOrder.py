
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postOrder_recursive(root):
	if root:
		postOrder_recursive(root.left)
		postOrder_recursive(root.right)
		print(root.val)

def postOrder(root):
	stack = []
	pre = None
	if root:
		stack.append(root)
		while stack:
			curr = stack[-1]
			if (not curr.left and not curr.right) or \
					(pre and (pre == curr.left or pre == curr.right)):
				print(curr.val)
				stack.pop()
				pre = curr
			else:
				if curr.right: stack.append(curr.right)
				if curr.left: stack.append(curr.left)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)

t1.right = t2
t2.left = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
postOrder(t1)
print()
postOrder_recursive(t1)
