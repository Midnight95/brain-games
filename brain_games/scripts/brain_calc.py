#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint, choice


def nums():
    num_1, num_2 = randint(0, 100), randint(0, 100)
    operation = choice(['+', '-', '*'])
    return [num_1, num_2, operation]


def calc():
    q1, q2, opr = nums()

    print('What is the result of the expression?')
    print(f'Question: {q1} {opr} {q2}')
    answer = int(input('Your answer: '))

    if opr == '+':
        correct_answer = q1 + q2
    elif opr == '-':
        correct_answer = q1 - q2
    else:
        correct_answer = q1 * q2

    return answer, correct_answer


def game(name):
    for _ in range(4):
        answer, correct_answer = calc()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(.'
                  f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}")
            break
    else:
        print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game(name)


if __name__ == '__main__':
    main()
