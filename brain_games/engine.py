from brain_games.cli import welcome_user


def start_game(module):
    name = welcome_user()
    print(module.MESSAGE)

    for _ in range(3):
        answer, correct_answer = module.generate_question()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}")
            return
    else:
        print(f'Congratulations, {name}!')
