from typing import List
from collections import deque

class Solution:

    def build_graph(self, adj_list):
        self.graph = {}

        for each in adj_list:
            u, v = each
            adj = self.graph.get(v, set())
            adj.add(u)
            self.graph[v] = adj

    def find_ready_node(self):
        for i in range(len(self.indegrees)):
            if self.indegrees[i] == 0:
                return i
        return -1

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True

        self.indegrees = [0 for _ in range(numCourses)]
        self.build_graph(prerequisites)
        print(f"indegrees {self.indegrees}")
        print(f"graph {self.graph}")

        for each in prerequisites:
            u, _ = each
            self.indegrees[u] += 1

        queue = deque()

        ready_idx = self.find_ready_node()
        if ready_idx == -1:
            return False

        queue.append(ready_idx)

        while queue:
            node = queue.popleft()
            if node == -1:
                return False
            print(f"processing node {node}")
            self.indegrees[node] = -1

            # dec adjacent node indegrees
            for adj in self.graph.get(node, []):
                self.indegrees[adj] -= 1

            ready_idx = self.find_ready_node()
            if ready_idx != -1:
                queue.append(ready_idx)

        # return all([indegree == -1 for indegree in self.indegrees])

            # 

        



s = Solution()

test = (2, [[1,0],[0,1]])
assert s.canFinish(*test) == False, "1"
test = (2, [[1,0]])
assert s.canFinish(*test) == True, "2"
test = (4, [[1, 0], [2, 1], [3, 2]])
assert s.canFinish(*test) == True, "3"
test = (3, [[1, 0], [2, 1], [0, 2]])
assert s.canFinish(*test) == False, "4"
test = (5, [[1,4],[2,4],[3,1],[3,2]])
assert s.canFinish(*test) == True, "5"
