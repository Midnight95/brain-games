from random import randint, choice

MESSAGE = 'What is the result of the expression?'
RANGE = (0, 50)


def start_game():
    num_1, num_2, = str(randint(*RANGE)), str(randint(*RANGE))
    operation = choice(['+', '-', '*'])

    question = ' '. join([num_1, operation, num_2])

    correct_answer = str(eval(question))

    return question, correct_answer

