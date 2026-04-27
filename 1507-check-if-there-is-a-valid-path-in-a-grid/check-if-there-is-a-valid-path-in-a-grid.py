from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions: up, down, left, right
        directions = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }
        
        # Opposite direction check
        def is_connected(x, y, nx, ny):
            for dx, dy in directions[grid[nx][ny]]:
                if nx + dx == x and ny + dy == y:
                    return True
            return False
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return True
            
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if is_connected(x, y, nx, ny):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False
        