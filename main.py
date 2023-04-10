from pyamaze import maze,agent,textLabel,COLOR
from bfs import BFS
from Astar import aStar
from dfs import DFS
import mdp
from timeit import timeit
if __name__=='__main__':
    x=input("Input the width of maze: ")
    y=input("Input the height of maze: ")
    myMaze = maze(int(x), int(y))
    myMaze.CreateMaze(loopPercent=100)
    searchPath,shortestPath = DFS(myMaze)
    textLabel(myMaze, 'Shortest Path Length', len(shortestPath) + 1)
    textLabel(myMaze, 'Search Path Length', len(searchPath) + 1)
    print("length of shortest path: ", len(shortestPath)+1)
    print("search path length", len(searchPath)+1)
    a = agent(myMaze, footprints=True, color=COLOR.cyan, filled=True)
    b = agent(myMaze, footprints=True, color=COLOR.yellow)
    myMaze.tracePath({a: searchPath}, delay=100)
    myMaze.tracePath({b: shortestPath}, delay=100)
    t1 = timeit(stmt='DFS(myMaze)', number=100, globals=globals())
    textLabel(myMaze, 'Time Cost: ', t1)
    print("time cost: ", t1)
    myMaze.run()