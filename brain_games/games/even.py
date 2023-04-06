from random import randint

MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE = (0, 100)


def is_even(num):
    return num % 2 == 0


def start_game():
    question = randint(*RANGE)

    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
