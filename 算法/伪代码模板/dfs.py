# -*- coding: utf-8 -*-
"""深度优先搜索
非递归 借助栈
"""
visited = set()


def DFS(tree):
    """非递归写法"""
    if tree.root is None:
        return []
    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.append(node)

        process(node)
        nodes = generate_related_nodes(node)
        stack.append(nodes)

    # other processing work


def dfs(tree):
    if tree.root is None: return []
    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        process(node)

        nodes = generate_related_nodes(node)
        stack.push(nodes)
    # other processing work


def dfs(node, visited):
    """非递归"""
    if node in visited: return

    visited.add(node)

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
