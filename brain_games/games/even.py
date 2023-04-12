from random import randint

MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
START, END = 0, 100


def is_even(num):
    return num % 2 == 0


def build_question_answer_pair():
    question = randint(START, END)

    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
