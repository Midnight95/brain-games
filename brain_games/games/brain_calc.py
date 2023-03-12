from random import randint, choice

MESSAGE = "What is the result of the expression?"


def nums():
    num_1, num_2 = randint(0, 100), randint(0, 100)
    operation = choice(['+', '-', '*'])
    return [num_1, num_2, operation]


def calc():
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


def game(name):
    for _ in range(3):
        answer, correct_answer = calc()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}")
            return
    else:
        print(f'Congratulations, {name}!')
