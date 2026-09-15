class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    treasure.append((r, c))
        
        while treasure:
            r, c = treasure.popleft()
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                treasure.append((nr, nc))


       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # rows = len(grid)
        # cols = len(grid[0])
        # queue = deque()

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 0:
        #             queue.append((r, c))
        
        # directions = [
        #     [-1, 0],
        #     [1, 0],
        #     [0, 1],
        #     [0, -1]
        # ]
                    
        # while queue:
        #     r, c = queue.popleft()
        #     for dr, dc in  directions:
        #         nr = r + dr
        #         nc = c + dc

        #         if (nr < 0 or nr >= rows or nc < 0 or nc >= cols) or grid[nr][nc] != 2147483647:
        #             continue 
        #         grid[nr][nc] = grid[r][c] + 1
        #         queue.append((nr, nc))
        
        
        
        
        # rows = len(grid)
        # cols = len(grid[0])
        # queue = deque()

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 0:
        #             queue.append((r, c))
        # directions = [
        #     (-1, 0),  # up
        #     (1, 0),   # down
        #     (0, -1),  # left
        #     (0, 1)    # right
        # ]

        # while queue:
        #         r, c = queue.popleft()

        #         for dr, dc in directions:
        #             nr = r + dr
        #             nc = c + dc

        #             if (nr < 0 or nr >= rows or
        #             nc < 0 or nc >= cols or
        #             grid[nr][nc] != 2147483647):
        #                 continue
                    
        #             grid[nr][nc] = grid[r][c] + 1
                    # queue.append((nr, nc))



      

        