"""
⬅️ We have provided a union_find.py file under the "Files" tab 
of this widget. You can use this file to build your solution.
"""
from collections import deque

class UnionFind:

    # Initializing the parent list and count variable by traversing the grid
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    # Function to find the root parent of a node
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Function to connect components
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

    def print_uf(self):
        for n1, n2 in zip(self.parent, self.rank):
            print(f'({n1},{n2})')
    # Function to return the number of conencted components consisting of "1"s
    def get_count(self):
        return self.count

def num_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    uf = UnionFind(grid)
    island_cnt = 0
    uf.print_uf()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                # Check neighbors (down, right)
                    for dr, dc in [(0, 1), (1, 0)]:
                        nr, nc = r + dr, c + dc

                        # If a neighbor is valid and also land, union the cells
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            uf.union(r * cols + c, nr * cols + nc)
    
    print("post union:")
    uf.print_uf()
    return uf.get_count()

num_islands([
        ['1', '1', '1'],
        ['0', '1', '0'],
        ['1', '0', '0'],
        ['1', '0', '1']
    ])

def fill_island(grid, r, c):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    queue = deque([(r,c)])
    while queue:
        row,col = queue.popleft()
        if grid[row][col] == "1":
            grid[row][col] = "0"
            
        for dir in range(4):
            newx = row + dx[dir]
            newy = col + dy[dir]
            if newx >= 0 and newx < len(grid) and newy >=0 and newy < len(grid[0]) and grid[newx][newy]=="1":
                queue.append((newx,newy))

def num_islands_02(grid):
    rows = len(grid)
    cols = len(grid[0])
    island_cnt = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                island_cnt += 1
                # print(island_cnt)
                fill_island(grid, r, c)
                
    return island_cnt
