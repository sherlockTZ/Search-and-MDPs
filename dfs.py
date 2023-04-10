
def DFS(m):
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    searchPath=[]
    while len(frontier)>0:
        tempCell=frontier.pop()
        searchPath.append(tempCell)
        if tempCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[tempCell][d]==True:
                if d =='E':
                    child=(tempCell[0],tempCell[1]+1)
                if d =='W':
                    child=(tempCell[0],tempCell[1]-1)
                if d =='N':
                    child=(tempCell[0]-1,tempCell[1])
                if d =='S':
                    child=(tempCell[0]+1,tempCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=tempCell
        if poss>1:
            m.markCells.append(tempCell)
    shortestPath={}
    cell=m._goal
    while cell!=start:
        shortestPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return searchPath,shortestPath