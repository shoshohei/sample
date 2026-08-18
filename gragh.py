
class Maze:
    def __init__(self, width, height, breakNum=0):
        self.width = width
        self.height = height
        self.Cells = [[Cell(self, x, y) for x in range(width)] for y in range(height)]
        self.startCell = None
        self.goalCell = None
        self.curCell = None
        self.pathOut = True
        self.breakNum = breakNum

    def generate(self, maker = "穴掘り法", start = None, goal=None, isPerfect = False):
        self.mazeInit()
        
        if start == None:
            start = self.getCell(random.randint(0, self.width-1), random.randint(0, self.height-1))
        if goal == None:
            goal = start
            while start==goal:
                goal = self.getCell(random.randint(0, self.width-1), random.randint(0, self.height-1))
        
        self.startCell = start
        self.goalCell = goal
        if maker=="穴掘り法":
            q = [start]
            start.visit()

            while q:
                cur = q[-1]
                candidate = []
                neighbors = self.neighbors(cur)
                for dir, neighbor in neighbors:
                    if not neighbor.visited: candidate.append((dir, neighbor))

                if candidate:
                    dir, neighbor = random.choice(candidate)
                    self.connect(cur, neighbor, dir)
                    q.append(neighbor)
                    neighbor.visit()
                else:
                    q.pop()

        elif maker=="Prim":
            frontier = [n for _, n in self.neighbors(start)]
            start.visit()
            while frontier:
                nxt = random.choice(frontier)
                frontier.remove(nxt)

                visited_neighbors = []
                for (dir, neighbor) in self.neighbors(nxt):
                    if neighbor.visited:
                        visited_neighbors.append((dir, neighbor))
                        
                dir, neighbor = random.choice(visited_neighbors)
                self.connect(nxt, neighbor, dir)
                nxt.visit()

                for (dir, neighbor) in self.neighbors(nxt):
                    if not neighbor.visited and neighbor not in frontier:
                        frontier.append(neighbor)

        elif maker=="Kruskal":
            uf = UnionFind(self.width*self.height)
            walls = []
            for y in range(self.height):
                for x in range(self.width):
                    cell = self.getCell(x,y)
                    if x+1<self.width:
                        walls.append((cell, self.getCell(x+1, y), Cell.E))
                    if y+1<self.height:
                        walls.append((cell, self.getCell(x, y+1), Cell.S))
            
            random.shuffle(walls)
            while walls:
                cell1, cell2, dir = walls.pop()
                if not uf.issame(cell1.flatten, cell2.flatten):
                    uf.union(cell1.flatten, cell2.flatten)
                    self.connect(cell1, cell2, dir)

        # if not isPerfect:
        #     for i in range(self.breakNum):
        #         cell = random.choice(random.choice(self.Cells))
        #         dir, neighbor = random.choice(self.neighbors(cell))
        #         self.connect(cell, neighbor, dir)
        if not isPerfect:
            closed_walls = []

            for y in range(self.height):
                for x in range(self.width):
                    cell = self.getCell(x, y)

                    if x + 1 < self.width and not cell.isOpen(Cell.E):
                        closed_walls.append((cell, self.getCell(x + 1, y), Cell.E))

                    if y + 1 < self.height and not cell.isOpen(Cell.S):
                        closed_walls.append((cell, self.getCell(x, y + 1), Cell.S))

            random.shuffle(closed_walls)

            for i in range(min(self.breakNum, len(closed_walls))):
                cell, neighbor, dir = closed_walls[i]
                self.connect(cell, neighbor, dir)


    def solve(self, solver = "bfs", isOutput=False):
        self.resetVisited()
        count = 0
        self.startCell.visit()
        parent = {}
        parent[self.startCell] = None
        if solver=='bfs' or solver=='dfs':
            queue = deque([self.startCell])
            while queue:
                if solver=="bfs":
                    cur = queue.popleft()
                elif solver=="dfs":
                    cur = queue.pop()
                count += 1
                self.curCell = cur
                if cur ==self.goalCell:
                    path = []
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    path.reverse()
                    # print(f"Goal!{count}")
                    return count, path
                else:
                    for dir, (dx, dy, opposite) in DIRS.items():
                        nx, ny = cur.x+dx, cur.y+dy
                        nxtCell = self.getCell(nx, ny)
                        if cur.isOpen(dir) and not nxtCell.visited:
                            nxtCell.visit()
                            parent[nxtCell] = cur
                            queue.append(nxtCell)
                if isOutput:
                    self.visualizeMaze()
                    input()
        elif solver=='astar':
            g_score = {}
            g_score[self.startCell] = 0
            open_list = []
            heapq.heapify(open_list)
            heapq.heappush(open_list, (g_score[self.startCell]+self.Manhatan(self.startCell), self.startCell.flatten, self.startCell))
            while open_list:
                cost, _, nxt = heapq.heappop(open_list)
                nxt.visit()
                count += 1
                if nxt == self.goalCell:
                    path = []
                    cur = nxt
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    path.reverse() 
                    # print("Goal!")
                    return count, path
                for dir, neighbor in self.neighbors(nxt):
                    if not nxt.isOpen(dir): continue
                    curCost = g_score.get(neighbor, 1e8)
                    newCost = g_score[nxt]+1
                    if curCost > newCost:
                        g_score[neighbor] = newCost
                        parent[neighbor] = nxt
                        heapq.heappush(open_list, (g_score[neighbor]+self.Manhatan(neighbor),neighbor.flatten, neighbor))
        

    def Manhatan(self, cell, target=None):
        if target is None:
            target = self.goalCell
        return abs(target.x-cell.x)+abs(target.y-cell.y)


    def isBounds(self, x, y):
        return 0<=x<self.width and 0<=y<self.height
    
    def getCell(self, x, y):
        if self.isBounds(x, y):
            return self.Cells[y][x]
        return None

    def neighbors(self, cell):
        res = []

        for dir, (dx, dy, opposite) in DIRS.items():
            nx, ny = cell.x + dx, cell.y + dy
            if self.isBounds(nx, ny):
                neighbor = self.getCell(nx, ny)
                res.append((dir, neighbor))
        return res

    def connect(self, cell1, cell2, dir):
        dx, dy , opposite = DIRS[dir]
        cell1.open(dir)
        cell2.open(opposite)

    def disConnect(self, cell1, cell2, dir):
        dx, dy, opposite = DIRS[dir]
        cell1.close(dir)
        cell2.close(opposite)

    def visualizeMaze(self, path=None):
        res = [[" " for _ in range(2*self.width-1)] for _ in range(2*self.height-1)]
        for y in range(self.height):
            for x in range(self.width):
                cell = self.getCell(x,y)
                if cell.visited:
                    res[2*y][2*x] = "."
                else:
                    res[2*y][2*x] = "+"    
                for dir, (dx, dy, _) in DIRS.items():
                    nx, ny = 2*x+dx, 2*y+dy
                    if 0<=nx<2*self.width-1 and 0<=ny<2*self.height-1:
                        pathDisplay = "-" if dir==Cell.W or dir==Cell.E else "|"
                        if self.pathOut:
                            res[ny][nx] = pathDisplay if cell.isOpen(dir) else " "
                        else:
                            res[ny][nx] = pathDisplay if not cell.isOpen(dir) else " "
        if self.startCell is not None:
            x, y = self.startCell.x, self.startCell.y
            res[2*y][2*x] = "S"
        if self.goalCell is not None:
            x, y = self.goalCell.x, self.goalCell.y
            res[2*y][2*x] = "G"
        if self.curCell is not None:
            x, y = self.curCell.x, self.curCell.y
            res[2*y][2*x] = "@"

        if path is not None:
             for p in path:
                x, y = p.Pos()
                if p == self.startCell:
                    res[2*y][2*x] = "S"
                elif p == self.goalCell:
                    res[2*y][2*x] = "G"
                else:
                    res[2*y][2*x] = "\033[31m*\033[0m"
        for i in res:
            print("".join(i))

    def resetVisited(self):
        self.curCell = None
        for cell in self.Cells:
            for c in cell:
                c.visited = False

    def mazeInit(self):
        self.resetVisited()
        for y in range(self.height):
            for x in range(self.width):
                cell = self.getCell(x,y)
                for d,n in self.neighbors(cell):
                    self.disConnect(cell1=cell, cell2=n, dir=d)

class Cell:
    N = 1
    S = 2
    E = 4
    W = 8
    def __init__(self, maze, x, y):
        self.maze = maze
        self.dirOpen = 0
        self.x = x
        self.y = y
        self.flatten = maze.width*y+x
        self.visited = False

    def open(self, dir):
        self.dirOpen |= dir

    def close(self, dir):
        self.dirOpen &= ~dir

    def isOpen(self, dir):
        return (self.dirOpen & dir) != 0
    
    def visit(self):
        self.visited = True

    def Pos(self):
        return self.x, self.y

class UnionFind():
    def __init__(self, num):
        self.cells = list(range(num))

    def union(self, cell1, cell2):
        root1 = self.find(cell1)
        root2 = self.find(cell2)
        if root1!=root2: self.cells[root1] = root2

    def find(self, num):
        root = num
        while root!=self.cells[root]:
            root = self.cells[root]
        self.cells[num]  = root
        return root
    
    def issame(self, num1, num2):
        return self.find(num1)==self.find(num2)

DIRS = {
    Cell.N:(0, -1, Cell.S),
    Cell.S:(0, 1, Cell.N),
    Cell.E:(1, 0, Cell.W),
    Cell.W:(-1, 0, Cell.E),
}

def MazeAndSolveTest(maker=None, solver=None):
    nums = {}
    pathL = {}
    for s in solver:
        for m in maker:
            nums[m+s] = []
            pathL[m+s] = []
    for n in range(experienceNum):
        for m in maker:
            maze.generate(
                    maker=m,
                    start=maze.getCell(0, 0),
                    goal=maze.getCell(maze.width-1, maze.height-1),
                    isPerfect=False
                )
            for s in solver:
                numIter, path = maze.solve(solver=s)
                nums[m+s].append(numIter)
                pathL[m+s].append(len(path))
                # print(m+s+str(n))
    
    for m in maker:
        for s in solver:
            print('{}:試行回数={:.2f}\tパス長:{:.2f}\n'.format(m+s, sum(nums[m+s])/experienceNum, sum(pathL[m+s])/experienceNum))
import random
from collections import deque
import heapq

experienceNum = 30
width = 20
height = 20
randBreakNum = 10*width
maze = Maze(width, height, breakNum=randBreakNum)
makers = ['穴掘り法', 'Prim', 'Kruskal']
solves = ['bfs', 'dfs', 'astar']
MazeAndSolveTest(maker=makers, solver=solves)

# maze.generate(maker="Kruskal", start=maze.getCell(0, 0), goal=maze.getCell(maze.width-1, maze.height-1))
# maze.visualizeMaze()
# maze.resetVisited()
# numIter, path = maze.solve(solver="astar")
# maze.visualizeMaze(path=path)
