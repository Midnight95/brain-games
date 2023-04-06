import prompt
ROUNDS = range(3)


def play(module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(module.MESSAGE)

    for _ in ROUNDS:
        question, correct_answer = module.start_game()

        print(f'Question: {question}')
        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(.'
                  f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return
    else:
        print(f'Congratulations, {name}!')
