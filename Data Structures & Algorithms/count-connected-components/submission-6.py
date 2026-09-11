class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        count = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(i):
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
        
        # parent = list(range(n))c
        # count = n
        # def find(x):
        #     while parent[x] != x:
        #         x = parent[x]
        #     return x
        
        # def union(u, v):
        #     nonlocal count
        #     root_u, root_v = find(u), find(v)
        #     if root_u != root_v:
        #         parent[root_u] = root_v
        #         count -= 1
        # for u, v in edges:
        #     union(u, v)
        # return count

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = n
        # parent = list(range(n))

        # def find(x):
        #     while parent[x] != x:
        #         x = parent[x]
        #     return x
        
        # def union(u, v):
        #     nonlocal count
        #     node_u, node_v = find(u), find(v)
        #     if node_u != node_v:
        #         parent[node_u] = node_v
        #         count -= 1
        
        # for u, v in edges:
        #     union(u, v) 
    
        # return count


        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = n
        # parent = list(range(n))

        # def find(x):
        #     while parent[x] != x:
        #         x = parent[x]
        #     return x

        # def union(u, v):
        #     nonlocal count
        #     node_u = find(u)
        #     node_v = find(v)

        #     if  node_v != node_u:
        #         parent[node_u] = node_v
        #         count -= 1


        # for u, v in edges:
        #     union(u, v)
        # return count

        