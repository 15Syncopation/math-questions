# Handle all user interaction with geometry

import geometry
import random

# Random modules
RANDOM_NUMBER = random.randint
RANDOM_PICK = random.choice


questions = []


def generate(number_of_questions, shape):
	exit_status = 0
	while exit_status < number_of_questions:
		exit_status += 1
		generate_question = RANDOM_NUMBER(1, 10)
		
		if exit_status < number_of_questions:
			questions.append(generate_question)
			print(f'Question {exit_status}: {generate_question}')

		elif exit_status == number_of_questions:
			questions.append(generate_question)
			print(f'Question {exit_status}: {generate_question}')


def interaction():
	user_total_questions = int(input('> '))
	user_shape = input('Shape: ')

	generate(user_total_questions, user_shape)
	exit_status = 0
	while exit_status < len(questions):
		for number in questions:
			print(Square.area(number))
			UI = int(input('Answer: '))
			if UI == Square.area(number):
				status += 1
				print(0)
			elif UI != Square.area(number):
				print('Wrong Answer')
				while UI != Square.area(number):
					UI = int(input('Answer: '))
					if UI == Square.area(number):
						status += 1
						break


#interaction()
#generate(2)

def woy():
	return 0
di = {'aaa': woy()}
