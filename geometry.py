# 21/02/2021

import math
import random


class Square():
	def area(side):
		return side * side


geometry_problem = []
def generate(exit_num):
	status = 0
	while status < exit_num:
		status += 1
		sideg = random.randint(1, 10)
		
		if status < exit_num:
			geometry_problem.append(sideg)
			print(f'Side: {sideg}')

		elif status == exit_num:
			geometry_problem.append(sideg)
			print(f'Side: {sideg}')


# FIX!
# Make sure that the i never changed until the input is correct
def interaction():
	user_exit_num = int(input('> '))
	generate(user_exit_num)
	status_i = 0
	while status_i < len(geometry_problem):
		for i in geometry_problem:
			print(Square.area(i))
			UI = int(input('Area: '))
			if UI == Square.area(i):
				status_i += 1
				print(0)
			else:
				print(1)


interaction()
#generate(2)
