import prompt
ROUNDS_COUNT = 3


def play_game(module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(module.MESSAGE)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = module.build_question_answer_pair()

        print(f'Question: {question}')
        answer = input('Your answer: ')

        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(.'
                  f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return

        print('Correct!')

    else:
        print(f'Congratulations, {name}!')
