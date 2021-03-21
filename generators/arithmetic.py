import random
import operator

# Evaluate the questions

def generate(total_questions, total_constants):
	math_operators = ['+', '-', '*', '/']
	
	global questions
	global answers
	
	questions = {}
	question_number = 0
	
	answers = []
	
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
	
	if len(questions) != 0:
		for answer in questions.values():
			answers.append(eval(answer))
	
	return 0


def show(show_questions, show_answers, return_both):
	if show_questions == True:
		return questions
		
	elif show_answers == True:
		return answers
	
	elif return_both == True:
		return questions, answers



generate(4, 2)
print(show(False, False, True))
