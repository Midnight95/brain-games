from random import randint, choice

MESSAGE = 'What is the result of the expression?'
OPERATION = ['+', '-', '*']
RANGE = (0, 50)


def game_logic():
    num_1, num_2, = randint(*RANGE), randint(*RANGE)
    operation = choice(OPERATION)

    print(f'Question: {num_1} {operation} {num_2}')
    answer = int(input('Your answer: '))

    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    elif operation == '*':
        correct_answer = num_1 * num_2

    return answer, correct_answer
