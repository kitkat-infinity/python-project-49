import prompt
from brain_games.cli import welcome_user

ROUNDS = 3

def play_round(number, correct_answer):
    print(f"Question: {number}")
    answer = prompt.string('Your answer: ')
    if correct_answer == answer:
        print('Correct!')
        return True
    
    print(f"{answer} is wrong answer ;(. \
Correct answer was {correct_answer}")
    return False
 

def play_game(game):
    name = welcome_user()
    print(game.GAME_TASK)
    count = 0
    while count < ROUNDS:
        number, correct_answer = game.get_answer_and_question()
        if play_round(number, correct_answer):
            count += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if count == ROUNDS:
        print(f'Congratulations, {name}!')
