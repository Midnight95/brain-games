from random import randint, choice

MESSAGE = "What is the result of the expression?"


def nums():
    num_1, num_2 = randint(0, 100), randint(0, 100)
    operation = choice(['+', '-', '*'])
    return [num_1, num_2, operation]


def game_logic():
    n1, n2, opr = nums()

    print(f'Question: {n1} {opr} {n2}')
    answer = int(input('Your answer: '))

    if opr == '+':
        correct_answer = n1 + n2
    elif opr == '-':
        correct_answer = n1 - n2
    else:
        correct_answer = n1 * n2

    return answer, correct_answer
