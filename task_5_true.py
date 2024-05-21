
import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heap_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    node.left = heap_tree(heap, left_index)
    node.right = heap_tree(heap, right_index)
    return node

def heap_visual(heap_array):
    if not heap_array:
        print("Пусто")
        return
    heapq.heapify(heap_array)
    heap_tree_root = heap_tree(heap_array)
    draw_tree(heap_tree_root)

def generate_color_gradient(start_hex, end_hex, steps):
    def hex_to_rgb(hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(*rgb)

    start_rgb = hex_to_rgb(start_hex.strip('#'))
    end_rgb = hex_to_rgb(end_hex.strip('#'))

    gradient = []
    for step in range(steps):
        interpolated = [
            int(start_rgb[j] + (float(step) / (steps - 1)) * (end_rgb[j] - start_rgb[j]))
            for j in range(3)
        ]
        gradient.append(rgb_to_hex(tuple(interpolated)))
    return gradient

def dfs_with_colors(node, total_nodes):
    visited = []
    stack = [node]
    color_gradient = generate_color_gradient('#00008B', '#ADD8E6', total_nodes)
    
    step = 0

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            vertex.color = color_gradient[step]
            
            step += 1
            if vertex.right:
                stack.append(vertex.right)
            if vertex.left:
                stack.append(vertex.left)

    draw_tree(node)
    return visited

def bfs_with_colors(node, total_nodes):
    visited = []
    queue = deque([node])
    color_gradient = generate_color_gradient('#00008B', '#ADD8E6', total_nodes)
    
    step = 0

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            vertex.color = color_gradient[step]
            
            step += 1
            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)
            
    
    draw_tree(node)
    return visited
    


# Створення дерева
heap_array = [5, 25, 8, 1, 3, 29, 40]
heap_visual(heap_array)
heap_tree_root = heap_tree(heap_array)
total_nodes = len(heap_array)

print("DFS Обхід:")
dfs_visited = dfs_with_colors(heap_tree_root, total_nodes)
print("\nПослідовність вузлів в DFS:", [node.val for node in dfs_visited])

print("\nBFS Обхід:")
bfs_visited = bfs_with_colors(heap_tree_root, total_nodes)
print("\nПослідовність вузлів в BFS:", [node.val for node in bfs_visited])
