import prompt


def start_game(module):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print(module.MESSAGE)

    for _ in range(3):
        answer, correct_answer = module.generate_question()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    else:
        print(f'Congratulations, {name}!')
