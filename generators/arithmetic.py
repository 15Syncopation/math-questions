import random
import operator


def generate(total_questions, total_constants):
	math_operators = ['+', '-', '*', '/']
	global questions
	questions = {}
	question_number = 0
	
	generated_questions = 0
	generated_constants = 0
	
	
	if generated_questions < total_questions:
		while generated_questions < total_questions:
			if generated_constants == 0:
				generated_constants += 1
				question_number += 1
				questions[question_number] = str(random.randint(50, 1000)) + random.choice(math_operators)
			
			elif generated_constants != 0 and generated_constants < total_constants - 1:
				generated_constants += 1
				questions[question_number] += str(random.randint(50, 1000)) + random.choice(math_operators)
			
			elif generated_constants == total_constants - 1:
				generated_constants += 1
				questions[question_number] += str(random.randint(50, 1000))
			
			elif generated_constants == total_constants:
				generated_questions += 1
				generated_constants = 0
	
	
	return questions
