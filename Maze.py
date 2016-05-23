
import numpy as np

class Maze:

 maze=np.zeros((1,1))

 start_position = np.array([-1,-1],dtype=int)

 def __init__(self,maze)
   self.maze = maze
   self.start_position = np.array([-1,-1],dtype=int)

 
 def get_start_position(self):

	startPosition_2 = np.array([0,0],dtype=int)

 	if self.start_position[0] == -1 and self.start_position[1] == -1:

 		return self.start_position
 	else:
 		
 		for rowIndex in range(len(self.maze)):
 			for colIndex in range(len(self.maze)):
 				if self.maze[rowIndex][colIndex] == 2:
 					self.start_position = np.array([colIndex,rowIndex],dtype=int)
 					return np.array([colIndex,rowIndex],dtype=int)

 	return self.startPosition_2

 def get_position_value(self,x,y):
 	
 	if x < 0 or y < 0 or x >= len(self.maze) or y >= len(sel.maze):
  	 return 1
  	else:
  	 return self.maze[x][y]

 def is_wall(self,x,y):
 	return self.maze[x][y] == 1

 def get_max_x(self):
 	return len(self.maze[0])

 def get_max_y(self):
 	return len(self.maze)

 def score_route(self,route):
 	score = 0
 	sizeOfMaze = len(self.maze)+1
 	arangeX    = np.arange(sizeOfMaze)
 	visited    = np.logical_not(arangeX < sizeOfMaze)

 	for index in range(len(route)):
 		step = route[index]
 		if self.maze[step[1]][step[0]] == 3 and visited[step[1]][step[0]] == False:
 			score=score+1
 			visited[step[1]][step[0]]=True
 		else:
 			visited[step[1]][step[0]]=False

    return score
    




















