from random import randint

MESSAGE = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def generate_question():
    num = randint(0, 102)

    correct_answer = 'yes' if is_prime(num) else 'no'

    print(f'Question: {num}')
    answer = str(input('Your answer: '))

    return answer, correct_answer
