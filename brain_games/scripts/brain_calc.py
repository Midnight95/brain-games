#!/usr/bin/env python3
from brain_games.games.brain_games import welcome_user
from brain_games.games.brain_calc import game, MESSAGE


def main():
    name = welcome_user()
    print(MESSAGE)
    game(name)


if __name__ == '__main__':
    main()
