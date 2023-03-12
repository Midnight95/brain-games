from random import randint, choice

MESSAGE = "What number is missing in the progression?"


def game_logic():
    length = randint(5, 16)
    step = randint(1, 11)
    progression = [str(step * i) for i in range(1, length + 1)]

    correct_answer = (choice(progression))

    progression[progression.index(correct_answer)] = '..'
    print(f'Question: {" ".join(progression)}')
    answer = str(input('Your answer: '))

    return answer, correct_answer
