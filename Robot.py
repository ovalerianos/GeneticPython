
from Maze import *
import numpy as np

class Robot:
 
 x_position = 0
 y_position = 0
 maxMoves   = 0
 moves      = 0
 sensore_value  = 0
 sensore_actions = range(1)
 maze = Maze(np.array([0,0],dtype=int))
 route = range(1)
 heading   = Direction.UNKNOWN

 lst_direccion    = range(1)
 lst_sensor_value = range(1)



 def __init__(self,maze):
  self.maze = maze

 def run():
 	self.moves = self.moves + 1

 def get_next_action(self):
 	return self.sensore_actions[self.get_sensor_value()]

 def get_heading(self):
 	return self.heading

 def get_lst_direcction(self):
 	return self.lst_direccion

 def get_lst_sensdor_value(self):
 	return self.lst_sensor_value

 def get_sensor_value(self):
 	if self.sensore_value > -1:
 		return self.sensore_value

 	frontSensor,frontLeftSensor,frontRightSensor,leftSensor,rightSensor,backSensor=False
 	if self.get_heading() == Direction.NORTH:
 		frontSensor     = self.maze.is_wall(self.x_position , self.y_position-1)
 		frontLeftSensor = self.maze.is_wall(self.x_position-1 , self.y_position-1)





class Direction:
	NORTH   = "NORTH"
	EAST    = "EAST"
	SOUTH   = "SOUTH"
	WEST    = "WEST"
	UNKNOWN = "UNKNOWN"