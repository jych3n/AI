'''
Cocnepts in Artificial Intelligence
This program contains two uniformed searching methods, Depth Limited Search and Iterative Deepening Search
User will be able to input a starting point and a goal in the graph and get an output displaying the path taken
The graph in this program is dedicated to this program, and is alterable
@Author: Jun Yan Chen
@Version: 9.13.2021
'''

# Store the graph as an adjacent list
graph = {
    'a' : ['b', 'c', 'd'],
    'b' : ['e', 'f', 'g'],
    'c' : ['h', 'i'],
    'd' : ['n', 'j'],
    'e' : ['k','l'],
    'f': [],
    'g': ['m'],
    'h': [],
    'i': [],
    'j': [],
    'n': [],
    'k': ['n'],
    'l': [],
    'm': [],
    'n': []
}

# Depth Limited Search
# Return a path if goal is reached successfully, else return false
def DLS(start, goal, depth, path):
    # Add node to a list for solution
    path.append(start)
    # Return solution if goal is reached
    if start == goal:
        return path
    # End searching if user specified depth is reached
    if depth <= 0:
        return False
    # Check if goal is reached in child node recursively
    # Remove from solution list if goal is not reached
    for node in graph[start]:
        if DLS(node, goal, depth-1, path):
            return path
        else:
            path.pop()
    return False
  
# Iterative Deepening Search
# Return a path if goal is reached successfully, else return false
def IDS(start, goal):
    # Increment depth iteratively and call DLS with each depth
    # Print message if goal is not reached with depth i 
    for i in range(1, len(graph)-1):
        result = DLS(start, goal, i, path)
        if result:
            return result
        else:
            path.pop()
            print('IDS: path from ', start, ' to ', goal, '[depth ', i, ']: not found')
    return False

# key for exit/continue
quit = False

# Main menu
while not quit:
    # prompt user to choose between using DLS or IDS
    method = int(input('\nSelect a searching method 1)DLS 2)IDS: '))
    # new empty list as parameter for the searching methods
    path = list() 

    # Depth Limited Search       
    if method == 1:
        start, goal = input('Enter start and goal: ').split(' ')
        depth = int(input('Enter depth: '))
        resultDLS = DLS(start, goal, depth, path)
        if resultDLS:
            print("DLS: path from ", start, " to " , goal, " is ", ' - '.join(resultDLS), '\n')
        else:
            print("No path found.")

    # Iterative Deepening Search
    elif method == 2:
        start, goal = input('Enter start and goal: ').split(' ')
        resultIDS = IDS(start, goal)
        if resultIDS:
            print('IDS: path from ', start, ' to ', goal, '[depth ', len(resultIDS)-1, ']: found [', ' - '.join(resultIDS), ']\n')
    
    # User input is neither 1 or 2
    else:
        print("Invalid choice.")
    
    # prompt user to choose to continue or exit the program
    choice = int(input('Do you wish to continue? 1)Yes 2)No: '))
    if choice == 2:
        quit = True
        break

'''
Sample:
Select a searching method 1)DLS 2)IDS: 1
Enter start and goal: a n
Enter depth: 2
DLS: path from  a  to  n  is  a - d - n 

Do you wish to continue? 1)Yes 2)No: 1

Select a searching method 1)DLS 2)IDS: 2 
Enter start and goal: a n
IDS: path from  a  to  n [depth  1 ]: not found
IDS: path from  a  to  n [depth  2 ]: found [ a - d - n ]

Do you wish to continue? 1)Yes 2)No: 2
'''