from random import randint, choice

MESSAGE = 'What number is missing in the progression?'
RANGE_START, RANGE_END = 5, 16
STEP_START, STEP_END = 1, 11


def make_progression(step, length):
    return [str(step * i) for i in range(1, length + 1)]


def build_question_answer_pair():
    step = randint(STEP_START, STEP_END)
    length = randint(RANGE_START, RANGE_END)

    progression = make_progression(step, length)

    correct_answer = (choice(progression))

    progression[progression.index(correct_answer)] = '..'
    question = ' '.join(progression)

    return question, correct_answer
