from random import randint

# Game description
MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def question():
    num = randint(0, 100)
    proof = is_even(num)

    return num, proof


def game(name):
    for _ in range(3):
        num, proof = question()
        answer = input(f'Question: {num}\nYour answer: ')

        if answer != ('yes' if proof else 'no'):
            correct_answer = 'yes' if proof else 'no'
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            return
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')
