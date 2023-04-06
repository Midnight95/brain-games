from random import randint
from math import gcd

MESSAGE = 'Find the greatest common divisor of given numbers.'
RANGE = (0, 100)


def start_game():
    num1, num2 = randint(*RANGE), randint(*RANGE)
    correct_answer = str(gcd(num1, num2))

    question = ' '.join([str(num1), str(num2)])

    return question, correct_answer
