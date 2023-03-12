from random import randint
from math import gcd
MESSAGE = "Find the greatest common divisor of given numbers."


def generate_question():
    num1, num2 = randint(0, 100), randint(0, 100)
    correct_answer = gcd(num1, num2)

    print(f'Question: {num1} {num2}')
    answer = int(input('Your answer: '))

    return answer, correct_answer
