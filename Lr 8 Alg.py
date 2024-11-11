class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None  #  поддерево
        self.right = None

def in_order(node):
    if node is not None:
        in_order(node.left)  # Рекурсивно обходим левое поддерево
        print(node.key, end=' ') #формат выв
        in_order(node.right)

def pre_order(node):
    if node is not None:
        print(node.key, end=' ')
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.key, end=' ')

def build_tree(n, nodes):
    tree = [TreeNode(key) for key, _, _ in nodes]  # Создаем узлы дерева, _ left and right потомки.
    for i in range(n):
        _, left, right = nodes[i]  # Получаем информацию о текущем узле
        if left != -1:  # Если есть левый сын
            tree[i].left = tree[left]  # Устанавливаем левое поддерево
        if right != -1:
            tree[i].right = tree[right]
    return tree[0]  # Возвращаем корень дерева

# Чтение входных данных
n = int(input())  # Читаем количество узлов
nodes = [tuple(map(int, input().split())) for _ in range(n)] #tuple превращение в кортеж

root = build_tree(n, nodes)


in_order(root)
print()  #переход на нов строку
pre_order(root)
print()
post_order(root)
print()