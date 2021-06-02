class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        current_max = 0
        
        max_y = len(grid)
        max_x = len(grid[0])
        def valid_coords(coord):
            return coord[0] >= 0 and coord[0] < max_y and coord[1] >= 0 and coord[1] < max_x 
        
        stack = []
        
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 1:
                    stack.append([y,x])
                    
                    # DFS
                    count = 0
                    while stack:
                        y_d, x_d = stack.pop()
                        
                        if grid[y_d][x_d] == 1:
                            count += 1
                            coords = [[y_d, x_d-1], [y_d, x_d+1],
                                      [y_d-1, x_d], [y_d+1, x_d]]

                            for coord in coords:
                                if valid_coords(coord):
                                    stack.append(coord)

                        grid[y_d][x_d] = 0
                    
                    current_max = max(current_max, count)
                    
        return current_max