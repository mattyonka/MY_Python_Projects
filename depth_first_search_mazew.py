import random
import pygame
import time
#FOR NEXT TIME
#---DONE ----Build a function to use pygame to draw out maze
#Impliment solver routines
#What if part of the maze changes (arbitrarily), how does this change solution solving
#


#keep track of dictionary keys
#   keys should only have one value, its previous node
#   assign stack in order of pushed values to keep track of positions that are needed to explore

"""This program creates a maze and solves it based on the stack that the maze-solver creates. Also draws it in using pygame.

Maze is created using depth-first-search algorithm."""
# Define colours
white   = (255, 255, 255)
green = (0, 255, 0,)
blue = (0, 0, 255)
yellow = (255 ,255 ,0)

#spacing = how many pixels for each square
spacing = 40

#width and depth = number of squares
width = 10
depth = 10

# Pygame initialization values
widthPygame = 500
heightPygame = 600
FPS = 30

#x,y coordinates
def buildMaze(width,depth):
    #initializing variables
    maze = {}
    start = [0,0]
    current = start
    stack = []
    visited =[]
    stack.append(start)
    visited.append(start)

    #solution path using width and depth as ending parameters
    minPath = []
    pathFound = False
    end = [width,depth]

    #print("test")
    while len(stack) > 0:
        #print("1st loop test")

        #mapping out possible choices into cells[]
        curr_up = [current[0],current[1]-1]
        curr_down = [current[0],current[1]+1]
        curr_left = [current[0]-1,current[1]]
        curr_right = [current[0]+1,current[1]]
        cells =[]

        #checking if possible next cells are valid
        if curr_up not in visited and curr_up[1] >= 0:
            cells.append(curr_up)
        if curr_down not in visited and curr_down[1] <= depth:
            cells.append(curr_down)
        if curr_left not in visited and curr_left[0] >= 0:
            cells.append(curr_left)
        if curr_right not in visited and curr_right[0] <= width:
            cells.append(curr_right)

        #print(cells)

        if len(cells) ==0:
            stack.pop()
            if len(stack)!= 0:
                current = stack[len(stack)-1]
        else:
            #print("test")
            direc = random.choice(cells)

            #print(type(direc))
            #print(type(current))
            #Drawing in Pygame
            time.sleep(.02)
            drawCell(direc,current)

            maze[direc[0],direc[1]] = current[0],current[1]
            current = direc
            visited.append(current)
            stack.append(current)

            if stack[len(stack)-1] == end and pathFound == False:
                minPath = stack.copy()
                pathFound == True

    return maze,minPath



def drawGrid(numSquares,spacing,color):
    numLines = numSquares+1
    for i in range(0,numSquares+2,1):
            pygame.draw.line(screen,color,[i*spacing,0],[i*spacing,spacing*numLines])

    for j in range(0, numSquares+2, 1):
        pygame.draw.line(screen,color,[0,j*spacing],[spacing*numLines,j*spacing])
    pygame.display.update()

def drawCell(new,old):
    """Draws from old-> new in pygame
    where new and old are both two-value lists with [x,y] coordinates"""
    x = spacing*(old[0])
    y = spacing*(old[1])
    x_new = spacing*(new[0])
    y_new = spacing*(new[1])

    #used to create new values if bounds of the maze changes instead of permanant values
    #bounds change if its pushing into the x or y direction hence bound 1 and 2 being arbitrary names
    boundShort = spacing-1
    boundLong = (spacing*2)-1

   #draws in rectangle conditionally based on difference between x and y deltas between points
    if y_new > y:
        pygame.draw.rect(screen,blue,(x+1,y+1,boundShort,boundLong),0)
        pygame.display.update()
    if x_new > x:
        pygame.draw.rect(screen,blue,(x+1,y+1,boundLong,boundShort),0)
        pygame.display.update()
    if y_new < y:
        pygame.draw.rect(screen,blue,(x_new+1,y_new+1,boundShort,boundLong),0)
        pygame.display.update()
    if x_new < x:
        pygame.draw.rect(screen,blue,(x_new+1,y_new+1,boundLong,boundShort),0)
        pygame.display.update()

def drawSolution(maze_solved):
    """Draws solved maze (in list form) in order from start -> end position """
   #draws in rectangle conditionally based on difference between x and y deltas between points
    for i in range(0,len(maze_solved),1):
        #rect = (left,top,width,height)
        x = (spacing / 4) + (spacing * maze_solved[i][0])
        y = (spacing / 4) + (spacing * maze_solved[i][1])
        print(x,y)
        rect = (x,y,spacing/2,spacing/2)
        pygame.draw.rect(screen,yellow,rect,0)
        pygame.display.update()
        time.sleep(.02)

""" Not working at the moment. This would be a more robust algorithm to solve any maze rather than a maze that's currently being generated.
This algorithm would simply take any left turn and advance until the endpoint, like how they tell you to solve a corn maze.
def solveLeft(maze):
    #maze generation starts at 0,0 as a value and pushes forward one unit to use as the key,
    #as such the maze dictionary object starts at what is considered the "end" point of this
    #function

    end = [0,0]
    start = [width,depth]
    stack = []
    visited = []
    current = start

    while current != end:


    return solved
"""


# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((widthPygame, heightPygame))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()





#DrawingGrid

drawGrid(width,spacing,white)

maze,maze_solved= buildMaze(width,depth)
print(maze)
print(maze_solved)
drawSolution(maze_solved)

running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()