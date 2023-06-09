import random


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def number_prime(digit):
    for i in range(2, int(digit / 2 + 1)):
        if digit % i == 0:
            return 'no'
    return 'yes'


def get_answer_and_question():
    digit = random.randint(2, 100)
    question = digit
    correct_answer = str(number_prime(digit))
    return question, correct_answer


if __name__ == '__main__':
    get_answer_and_question()
