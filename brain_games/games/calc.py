from random import randint, choice

MESSAGE = 'What is the result of the expression?'
START, END = 0, 50


def build_question_answer_pair():
    num_1, num_2, = (randint(START, END)), (randint(START, END))
    operation = choice(['+', '-', '*'])

    question = f'{num_1} {operation} {num_2}'

    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    elif operation == '*':
        correct_answer = num_1 * num_2

    correct_answer = str(correct_answer)

    return question, correct_answer
