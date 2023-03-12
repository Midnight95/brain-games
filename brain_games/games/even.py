from random import randint

# Game description
MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def game_logic():
    num = randint(0, 100)

    print(f'Question: {num}')
    answer = input('Your answer: ')

    correct_answer = 'yes' if is_even(num) else 'no'
    return answer, correct_answer
