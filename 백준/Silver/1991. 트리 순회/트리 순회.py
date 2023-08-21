def preorder(n):
    if n != '.':
        print(n, end='')
        preorder(tree_dict[n][0])
        preorder(tree_dict[n][1])

def inorder(n):
    if n != '.':
        inorder(tree_dict[n][0])
        print(n, end='')
        inorder(tree_dict[n][1])

def postorder(n):
    if n != '.':
        postorder(tree_dict[n][0])
        postorder(tree_dict[n][1])
        print(n, end='')


V = int(input())
tree_dict = {}
for i in range(V):
    p, c1, c2 = input().split()
    tree_dict[p] = [c1, c2]
preorder('A')
print()
inorder('A')
print()
postorder('A')