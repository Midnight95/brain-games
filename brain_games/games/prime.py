from random import randint

MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START, END = 0, 102


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def build_question_answer_pair():
    question = randint(START, END)

    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
