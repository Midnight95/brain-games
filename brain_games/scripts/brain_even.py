#!/usr/bin/env python3
from brain_games.games.game import welcome_user
from brain_games.games.even import game, MESSAGE


def main():
    name = welcome_user()
    print(MESSAGE)
    game(name)


if __name__ == '__main__':
    main()
