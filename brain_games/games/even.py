from random import randint

# Game description
MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE = (0, 100)


def is_even(num):
    return num % 2 == 0


def game_logic():
    num = randint(*RANGE)

    print(f'Question: {num}')
    answer = input('Your answer: ')

    correct_answer = 'yes' if is_even(num) else 'no'
    return answer, correct_answer
