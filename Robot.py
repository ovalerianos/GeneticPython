
from Maze import *
import numpy as np

class Robot:
 
 x_position = 0
 y_position = 0
 maxMoves   = 0
 moves      = 0
 sensor_value  = 0
 sensor_actions = range(1)
 maze = Maze(np.array([0,0],dtype=int))
 route = range(1)
 heading   = Direction.UNKNOWN

 lst_direccion    = range(1)
 lst_sensor_value = range(1)



 def __init__(self,maze):
  self.maze = maze

 def run():
 	while True:
 		self.moves = self.moves + 1
 		if self.get_next_action() == 0:
 			return
 		if self.maze.get_position_value(x,y) == 4:
 			return
 		if self.moves > self.maxMoves:
 			return
 		#self.ma


 def make_next_action(self):

 	if self.get_next_action() == 1:
 		currentX = self.x_position
 		currentY = self.y_position

 	if Direction.NORTH == self.heading:
 		self.y_position = y_position - 1
 		if self.y_position < 0:
 			self.y_position = 0
 	elif Direction.EAST == self.heading:
 		




 def get_next_action(self):
 	return self.sensor_actions[self.get_sensor_value()]

 def get_heading(self):
 	return self.heading

 def get_lst_direcction(self):
 	return self.lst_direccion

 def get_lst_sensdor_value(self):
 	return self.lst_sensor_value

 def get_sensor_value(self):
 	if self.sensor_value > -1:
 		return self.sensor_value
 	frontSensor,frontLeftSensor,frontRightSensor,leftSensor,rightSensor,backSensor=False
 	if self.get_heading() == Direction.NORTH:
 		frontSensor     = self.maze.is_wall(self.x_position ,   self.y_position-1)
 		frontLeftSensor = self.maze.is_wall(self.x_position-1 , self.y_position-1)
 		frontRightSensor= self.maze.is_wall(self.x_position+1 , self.y_position-1)
 		leftSensor      = self.maze.is_wall(self.x_position-1 , self.y_position)
 		rightSensor     = self.maze.is_wall(self.x_position+1 , self.y_position)
 		backSensor      = self.maze.is_wall(self.x_position ,   self.y_position+1)
 	elif self.get_heading() == Direction.EAST:
 		frontSensor     = self.maze.is_wall(self.x_position+1 , self.y_position)
 		frontLeftSensor = self.maze.is_wall(self.x_position+1 , self.y_position-1)
 		frontRightSensor= self.maze.is_wall(self.x_position+1 , self.y_position+1)
 		leftSensor      = self.maze.is_wall(self.x_position ,   self.y_position-1)
 		rightSensor     = self.maze.is_wall(self.x_position ,   self.y_position+1)
 		backSensor      = self.maze.is_wall(self.x_position-1,  self.y_position)
 	elif self.get_heading() == Direction.SOUTH:
 		frontSensor     = self.maze.is_wall(self.x_position ,   self.y_position+1)
 		frontLeftSensor = self.maze.is_wall(self.x_position+1 , self.y_position+1)
 		frontRightSensor= self.maze.is_wall(self.x_position-1 , self.y_position+1)
 		leftSensor      = self.maze.is_wall(self.x_position+1 , self.y_position)
 		rightSensor     = self.maze.is_wall(self.x_position-1,  self.y_position)
 		backSensor      = self.maze.is_wall(self.x_position,    self.y_position-1)
 	else:
 		frontSensor     = self.maze.is_wall(self.x_position-1,  self.y_position)
 		frontLeftSensor = self.maze.is_wall(self.x_position-1 , self.y_position+1)
 		frontRightSensor= self.maze.is_wall(self.x_position-1 , self.y_position-1)
 		leftSensor      = self.maze.is_wall(self.x_position,    self.y_position+1)
 		rightSensor     = self.maze.is_wall(self.x_position,    self.y_position-1)
 		backSensor      = self.maze.is_wall(self.x_position+1,  self.y_position)
 	sensorVal = 0
 	if frontSensor == True:
 		sensorVal = sensorVal + 1
 	if frontLeftSensor == True:
 		sensorVal = sensorVal + 2
 	if frontRightSensor == True:
 		sensorVal = sensorVal + 4
 	if leftSensor == True:
 		sensorVal = sensorVal + 8
 	if rightSensor == True:
 		sensorVal = sensorVal + 16
 	if backSensor == True:
 		sensorVal = sensorVal + 32

 	self.sensor_value = sensorVal
 	return sensorVal

 
 def get_position_value(self,x,y):
 	 if x < 0 or y < 0 or x >= len(self.maze) or y >= len(self.maze[0]):
 	 	return 1

 	 return  self.maze[y][x]

 def is_wall(self,x,y):
 	return self.get_position_value(x,y) == 1







class Direction:
	NORTH   = "NORTH"
	EAST    = "EAST"
	SOUTH   = "SOUTH"
	WEST    = "WEST"
	UNKNOWN = "UNKNOWN"
