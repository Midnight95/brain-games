from random import randint, choice

MESSAGE = 'What is the result of the expression?'
START, END = 0, 50


def build_question_answer_pair():
    num_1, num_2, = str(randint(START, END)), str(randint(START, END))
    operation = choice(['+', '-', '*'])

    question = ' '. join([num_1, operation, num_2])

    correct_answer = str(eval(question))

    return question, correct_answer
