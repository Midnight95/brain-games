#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint


def is_even(num):
    return num % 2 == 0


def game():
    question = randint(0, 100)
    answer, condition = input(f'Question: {question}\nYour answer: '), is_even(question)

    if answer == 'yes' and condition or answer == 'no' and not condition:
        print('Correct!')
    else:
        correct_answer = 'yes' if is_even(question) else 'no'
        print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
        return ''



def start_game(name):
    for i in range(4):
        if game() == '':
            break
    else:
        print(f'Congratulations, {name}')


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(name)        

if __name__ == '__main__':
    main()
