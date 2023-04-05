from random import randint, choice

MESSAGE = 'What number is missing in the progression?'
LENGTH_RANGE = (5, 16)
STEP_RANGE = (1, 11)


def game_logic():
    length = randint(*LENGTH_RANGE)
    step = randint(*STEP_RANGE)
    progression = [str(step * i) for i in range(1, length + 1)]

    correct_answer = (choice(progression))

    progression[progression.index(correct_answer)] = '..'
    print(f'Question: {" ".join(progression)}')
    answer = str(input('Your answer: '))

    return answer, correct_answer
