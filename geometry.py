# 21/02/2021

# 24/02/2021
# Make a clean code.
# - Make it simple, stupid!
# - Meaningful variables name
# - Improve code until it's not necessary to write a obvious and redundant comments
# - Let one function do merely one task

import math
import random


class Square():
	def area(side):
		return side * side


geometry_questions = []
def generate(exit_num):
	status = 0
	while status < exit_num:
		status += 1
		sideg = random.randint(1, 10)
		
		if status < exit_num:
			geometry_questions.append(sideg)
			print(f'Side: {sideg}')

		elif status == exit_num:
			geometry_questions.append(sideg)
			print(f'Side: {sideg}')


def interaction():
	user_exit_num = int(input('> '))
	generate(user_exit_num)
	status = 0
	while status < len(geometry_questions):
		for i in geometry_questions:
			print(Square.area(i))
			UI = int(input('Area: '))
			if UI == Square.area(i):
				status += 1
				print(0)
			elif UI != Square.area(i):
				while UI != Square.area(i):
					UI = int(input('Area: '))
					if UI == Square.area(i):
						status += 1
						break


interaction()
#generate(2)
