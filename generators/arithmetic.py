import random
import operator


math_operators = ['+', '-', '*', '/']

def generate(exit_num):
	math_problem = []
	status = 0
	while status < exit_num:
		status += 1
		number_generator = str(random.randint(1, 10))
		
		if status < exit_num:
			math_problem.append(number_generator)
			math_problem.append(random.choice(math_operators))
		elif status == exit_num:
			math_problem.append(number_generator)
			math_problem = ' '.join(math_problem)
	
	print(math_problem)
	return eval(math_problem)
