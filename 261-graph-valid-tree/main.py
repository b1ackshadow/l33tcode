from typing import List

class Solution:
    def build_graph(self, edges):
        self.graph = {}

        for u, v in edges:
            self.graph[u] = self.graph.get(u, set()) | {v}
            self.graph[v] = self.graph.get(v, set()) | {u}

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 0:
            return False
        if n == 1:
            return True

        self.build_graph(edges)
        queue = []
        visited = [False] * n

        queue.append(0)

        while queue:
            node = queue.pop(0)
            if visited[node]:
                return False
            visited[node] = True

            for adj in self.graph.get(node, {}):
                if not visited[adj]:
                    queue.append(adj)


        return all(visited)





# Test cases
def test_valid_tree():
    solution = Solution()
    
    test_cases = [
        # Case 1: Basic tree
        (5, [[0, 1], [0, 2], [0, 3], [3, 4]], True),  # Simple valid tree
        # Case 2: Not a tree (cycle present)
        (5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]], False),  # Cycle
        # Case 3: Not connected
        (4, [[0, 1], [2, 3]], False),  # Disconnected components
        # Case 4: Single node, no edges
        (1, [], True),  # A single node is a valid tree
        # Case 5: Single edge
        (2, [[0, 1]], True),  # Two nodes with one edge
        # Case 6: Empty graph (invalid tree)
        (0, [], False),  # No nodes
        # Case 7: Graph with an extra edge
        (4, [[0, 1], [1, 2], [2, 3], [1, 3]], False),  # Extra edge makes a cycle
        # Case 8: Large valid tree
        (6, [[0, 1], [0, 2], [2, 3], [2, 4], [4, 5]], True),  # Larger tree
        # Case 9: Multiple nodes, no edges
        (4, [], False),  # Disconnected single nodes
    ]
    
    for i, (n, edges, expected) in enumerate(test_cases):
        result = solution.validTree(n, edges)
        assert result == expected, f"Test case {i+1} failed: {result} != {expected}"

# Run tests
test_valid_tree()


