from queue import PriorityQueue
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))
def aStar(m):
    start = (m.rows, m.cols)
    frontier = PriorityQueue()
    frontier.put((h(start, m._goal), h(start, m._goal), start))
    astarPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    searchPath = [start]
    while not frontier.empty():
        tempCell = frontier.get()[2]
        searchPath.append(tempCell)
        if tempCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[tempCell][d] == True:
                if d == 'E':
                    childCell = (tempCell[0], tempCell[1] + 1)
                elif d == 'W':
                    childCell = (tempCell[0], tempCell[1] - 1)
                elif d == 'N':
                    childCell = (tempCell[0] - 1, tempCell[1])
                elif d == 'S':
                    childCell = (tempCell[0] + 1, tempCell[1])

                temp_g_score = g_score[tempCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                if temp_f_score < f_score[childCell]:
                    astarPath[childCell] = tempCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    frontier.put((f_score[childCell], h(childCell, m._goal), childCell))

    shortestPath = {}
    cell = m._goal
    while cell != start:
        shortestPath[astarPath[cell]] = cell
        cell = astarPath[cell]
    return searchPath, shortestPath