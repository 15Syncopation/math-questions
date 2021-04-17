import random


math_operators = ['+', '-', '*', '/']
questions = []
answers = []


def generator(total_questions, total_constants):
	global questions
	global answers
	
	for question in range(total_questions):
		for constant in range(total_constants):
			random_number = str(random.randint(50, 1000))
			random_operator = random.choice(math_operators)
			
			if len(questions) == 0:
				questions.append(random_number + random_operator)
			
			elif constant == (total_constants - 1):
				questions[question] += random_number
				questions.append('')
				
				if question == (total_questions - 1):
					questions.pop(-1)
			
			else:
				questions[question] += random_number + random_operator
	
	
	if len(questions) != 0:
		for answer in questions:
			answers.append(eval(answer))



