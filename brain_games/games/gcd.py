from random import randint
from math import gcd

MESSAGE = 'Find the greatest common divisor of given numbers.'
START, END = 0, 100


def build_question_answer_pair():
    num1, num2 = randint(START, END), randint(START, END)
    correct_answer = str(gcd(num1, num2))

    question = ' '.join([str(num1), str(num2)])

    return question, correct_answer
