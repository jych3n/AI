'''
Jun Yan Chen
Concepts in Artificial Intelligence
A* Search Algorithm
Created: 9.19.2021
Update: 9.22.2021 Fixed the problem where the algorithm doesn't work for special board layout
                  Changed path storing method from using a list to backtracking parent node
Update: 9.23.2021 Changed data structure from list to heap/priority queue
'''
import math
import heapq
#The max row and col for the board
ROW = 19
COL = 19
 
# To store coordinates of a cell
class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y
 
# Node class contains information of a cell on the board
class Node:
    def __init__(self,pt: Point, g:float, parent):
        self.pt = pt  # coordinates
        self.f = 0
        self.g = g
        self.parent = parent

    # define less than for comparison of f(n)
    def __lt__(self, other):
      return self.f < other.f

# Check whether given coordinate is inside the board
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# A* Algorithm, parameter takes board, starting point, goal, 
# whether diagonal movement or not, and choice between Manhattan and Euclidean
def astar(board, start: Point, goal: Point, diagonal, Manhattan=True):

    # Decide neighbors
    if diagonal:
        # neighbors for diagonal movement
        rowNum = [1, -1, 1, 1, 0, -1, 0, -1]
        colNum = [-1, -1, 1, 0, 1, 0, -1, 1]
    else:
        # neighbors for non-diagonal movement
        rowNum = [1, 0,-1,0]
        colNum = [0, 1, 0,-1]
    
    # Set all coordinates to open(not visited)
    visited = [[False for i in range(COL)]
                       for j in range(ROW)]
     
    # Mark the starting point as visited
    visited[start.x][start.y] = True
     
    # Create a list to store nodes that are open
    open = []
     
    # Create starting node and add use it as the first element of the openlist
    s = Node(start,0,None)
    heapq.heapify(open)
    heapq.heappush(open,s)

    # decide the next step while openlist is not empty
    while open:
        # remove first node from openlist to review
        curr = open.pop(0) 
        pt = curr.pt

        # Return path if goal is reached by backtracking parent node
        if pt.x == goal.x and pt.y == goal.y:
            path = []
            current = curr
            while current is not None:
                path.append(current.pt)
                current = current.parent
            return path[::-1]  # Return reversed path
         
        # Check each neighbor
        # r = range of neighbors
        if diagonal: 
            r = 8
        else:
            r = 4
        for i in range(r):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
             
            # if neighbor is valid, has path and not visited yet, add it to the openlist.
            if (isValid(row,col) and board[row][col] != '#' and not visited[row][col]):
                visited[row][col] = True
                # Calculate h(n) for current neighbor
                if Manhattan:
                    h = abs(row - goal.x) + abs(col - goal.y)   #Manhattan
                else:
                    h = math.sqrt((row - goal.x)**2 + (col - goal.y)**2)   #Euclidean
                # Calculate g(n) for current neighbor
                if diagonal:
                    g = math.sqrt((row - curr.pt.x)**2 + (col - curr.pt.y)**2)
                else:
                    g = 1
                newCell = Node(Point(row,col), curr.g + g,curr)
                # Calculate f(n) for current neighbor
                newCell.f = g + h
                # Add cell to priority queue
                # The priority queue will always put the cell with lowest f(n) to the front
                heapq.heappush(open,newCell)
        
           
    # Return -1 if goal cannot be reached
    return -1
 
def main():
    # input
    board = [ 
        [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ],
        [ '#', 'A', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', '#' ],
        [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ]]
    '''
    # Use this board for further test
    board = [ 
        [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ],
        [ '#', 'A', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', 'B', '#' ],
        [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ]]
    '''
    start_x= 1
    start_y= 1
    goal_x= 18
    goal_y= 18

    # Create start and goal point
    start = Point(start_x,start_y)
    goal = Point(goal_x,goal_y)

    # Create two copies of board
    board1 = [x[:] for x in board]
    board2 = [x[:] for x in board]
    # Using the Euclidean heuristic
    # result for non-diagonal
    print('Euclidean Non-Diagonal A* Result:')
    result = astar(board1,start,goal,False,False)
    for a in result[1:-1]:
        board1[a.x][a.y] = '*'
    for i in board1:
        print (' '.join(i))

    # result for diagonal
    print('\nEuclidean Diagonal A* Result:')
    result = astar(board1,start,goal,True,False)
    for b in result[1:-1]:
        board2[b.x][b.y] = '*'

    for j in board2:
        print (' '.join(j))
     
    # Refresh boards
    board1 = [x[:] for x in board]
    board2 = [x[:] for x in board]

    # Using the Manhattan heuristic
    # result for non-diagonal
    print('Manhattan Non-Diagonal A* Result:')
    result = astar(board1,start,goal,False,True)
    for c in result[1:-1]:
        board1[c.x][c.y] = '*'
    for k in board1:
        print (' '.join(k))

    # result for diagonal
    print('\nManhattan Diagonal A* Result:')
    result = astar(board1,start,goal,True,True)
    for d in result[1:-1]:
        board2[d.x][d.y] = '*'

    for q in board2:
        print (' '.join(q))
main()
