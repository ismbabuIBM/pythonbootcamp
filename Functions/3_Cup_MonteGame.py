from random import shuffle

#shuffle a list
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

#take a player guess position
def player_guess():
    guess = 0
    while guess not in ['0', '1', '2']:
        guess = input('Pick your guess position from 0, 1, 2: ')
    return int(guess)

#play a game
def game(shuffled_list, player_guess):
    if shuffled_list[player_guess] == 'O':
        print('You guessed it right!!!')
    else:
        print('Better luck next time!')
        print(shuffled_list)

#game list
my_list = ['O', ' ', ' ']

#shuffle list function call
shuffled_list = shuffle_list(my_list)

#player guess position function call
guessPosition = player_guess()

#play a game function call
game(shuffled_list, guessPosition)