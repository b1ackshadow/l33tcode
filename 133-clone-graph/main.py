from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        # dict to node_idx -> node
        cloned_nodes = {}

        # for each node starting from root node of the graph, we need to 

        def dfs(node):
            cloned_nodes[node.val] = cloned_nodes.get(node.val, Node(node.val))
            cl_node = cloned_nodes[node.val]


            for n in node.neighbors:
                if n.val not in cloned_nodes:
                    dfs(n)
                cl_node.neighbors.append(cloned_nodes[n.val])

            # need to link the neighbors

        dfs(node)

        return cloned_nodes[1] if cloned_nodes else None

        


        


