class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = [i for i in range(n)] 

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False
            parent[root_u] = root_v
            return True
        
        for dx, dy in edges:
            if not union(dx, dy):
                return False
        return True
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # if len(edges) != n - 1:
        #     return False
        # parent = list(range(n))
        # def find(x):
        #     while parent[x] != x:
        #         x = parent[x]
        #     return x
        # def union(u, v):
        #     root_u, root_v = find(u), find(v)
        #     if root_u == root_v:
        #         return False
        #     parent[root_u] = root_v
        #     return True
        
        # for i in range(len(edges)):
        #     u, v = edges[i][0], edges[i][1]
        #     if not union(u, v):
        #         return False 
        # return True
        
        
        
