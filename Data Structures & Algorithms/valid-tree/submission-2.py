class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(u, v):
            node_u = find(u)
            node_v = find(v)

            if node_u == node_v:
                return False
            parent[node_u] = node_v
            return True


        for u, v in edges:
            if not union(u, v):
                return False
        return True