class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(u, v):
            nonlocal count
            node_u, node_v = find(u), find(v)
            if node_u != node_v:
                parent[node_u] = node_v
                count -= 1
        
        for u, v in edges:
            union(u, v) 
    
        return count


        
        
        
        
        
        
        
        
        
        
        
        
        
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

        