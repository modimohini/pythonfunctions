
#data = [[A,B], [A,C], [A,D], [B,E], [B,F]]

from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root)
#
#        __1
#       /   \
#      2     3
#     / \
#    4   5
#
print(root.inorder)
# [Node(4), Node(2), Node(5), Node(1), Node(3)]

print(root.preorder)
# [Node(1), Node(2), Node(4), Node(5), Node(3)]

print(root.postorder) 
# [Node(4), Node(5), Node(2), Node(3), Node(1)]

print(root.levelorder) 
# [Node(1), Node(2), Node(3), Node(4), Node(5)]

print(list(root)) # Equivalent to root.levelorder
# [Node(1), Node(2), Node(3), Node(4), Node(5)]