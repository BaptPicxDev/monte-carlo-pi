# -*- coding: utf-8 -*-

## Librairies 
import os 
import sys 
import math
import random
from datetime import datetime

## Environment 
PROJECT_PATH = os.getcwd()
SQUARE_SIDE_LENGTH = 1 
CIRCLE_DIAMETER = 1

CONFIGURATION = """
	---------------------------------
	This script, developped in python3, will try to aproximate the value of pi.
	In this example, we suppose we have a 1-meter side square.
	In the center of this square, we insert a 1-meter diameter circle.
	The aim is to calculate pi.  
	---------------------------------
"""

## Function 
def square() :
	perimeter = SQUARE_SIDE_LENGTH * 4 
	area = SQUARE_SIDE_LENGTH * SQUARE_SIDE_LENGTH
	return 0 

def circle() :
	perimeter = math.pi * CIRCLE_DIAMETER
	area = math.pi * (CIRCLE_DIAMETER * CIRCLE_DIAMETER) / 4 
	return 0

if __name__ == '__main__' :
	start = datetime.now()
	print(CONFIGURATION)
	tot_circle, n_iter = 0, 100000
	for i in range(n_iter) :
		x_pos = random.uniform(0, 1)
		y_pos = random.uniform(0, 1)
		distance = x_pos ** 2 + y_pos**2
		if distance <= CIRCLE_DIAMETER**2 :
			tot_circle+=1
	print("Using Monte-Carlo method, with {} iterations, we approximate pi = {}.\n".format(n_iter, 4*tot_circle/n_iter))
	print("It takes {} seconds to reach the end of the code.".format((datetime.now() - start).seconds))