from collections import deque
def BFS(maze):
    start=(maze.rows,maze.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    searchPath=[]
    while len(frontier)>0:
        tempCell=frontier.popleft()
        if tempCell==maze._goal:
            break
        for d in 'ESNW':
            if maze.maze_map[tempCell][d]==True:
                if d=='E':
                    childCell=(tempCell[0],tempCell[1]+1)
                elif d=='W':
                    childCell=(tempCell[0],tempCell[1]-1)
                elif d=='S':
                    childCell=(tempCell[0]+1,tempCell[1])
                elif d=='N':
                    childCell=(tempCell[0]-1,tempCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = tempCell
                searchPath.append(childCell)
    shortestPath={}
    cell=maze._goal
    while cell!=(maze.rows,maze.cols):
        shortestPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return searchPath,shortestPath