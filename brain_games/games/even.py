import random


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_task():
    number = random.randint(1, 100)
    correct_answer = str(is_even(number))
    return number, correct_answer
