import random

# This function prints the characters in a list right next to each other.
def print_list(mylist):
    for i in mylist:
        print(i, end='')
    print('')

# This function adds a new high score to the "high_scores.txt" file.
# In this version its not actually a high score. If the player wins no matter his score, he can save his result.
# The score is computed by 'number_of_lives*1000'.
def add_high_score(number_of_lives):
    f = open('high_scores.txt', 'a')
    name=input("Your name: ")
    f.write(name + ' ' + str(number_of_lives*1000) + '\n')
    f.close()


is_game_over = False   # A logical variable to decide when the game is over.
number_of_lives=5      # Number of guesses in the game.


# These are the words the game can choose from
words=['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']

# These are the valid characters that can be guessed during the game
valid_characters=['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

thought_word=random.choice(words)
guess_list=['_ ']*len(thought_word)  # This list will represent the thought word. We initialize it with the '_ ' strings
                                     # and as the player guesses the letters we change them.

guessed_characters=[]                # This is a list to store the characters the player already guessed.

print('I thought of a word.')
print_list(guess_list)


# This cycle will ask the player guess characters until the game is over. Either the player guessed the word or he lost
#  all his lives.
while(is_game_over == False):

    char=input("Please enter a letter (a-z) or a number (0-9): ")   # Asking for a character from the player.

    # Check if the user entered a valid character. An input from the user is invalid if it is
    if len(char)!=1:    # not one character
        print('Please only type one character!')

    elif char not in valid_characters: # not in 'valid_characters'
        print('That character is not valid!')

    elif char in guessed_characters:    # was already guessed
        print("You already guessed that character.")
        print("Characters already guessed: ", end='')
        print(guessed_characters)

    # If the character is valid
    else:
        guessed_characters.append(char)     # add it to the 'guessed_characters'

        # If the character is in the 'thought_word'
        if char in thought_word:
            indexes=[index for index, value in enumerate(thought_word) if value == char] # get the indices where it occurs
            for i in indexes:
                guess_list[i]=char + ' '    # and change the '_ ' in those places to the letter

             #If all the '_ ' characters have been replaced
            if '_ ' not in guess_list:
                print('Congratulations! You won!')  # The player won.
                is_game_over = True
                print_list(guess_list)
                add_high_score(number_of_lives)
                break
            print_list(guess_list)
            print("Characters already guessed: ", end='')
            print(guessed_characters)

        # If the character is not in the 'thought_word'
        else:
            print("That character is not in the word.")
            number_of_lives -= 1                                # the player loses a life
            print("You have " + str(number_of_lives) + " lives left.")
            print_list(guess_list)
            print("Characters already guessed: ", end='')
            print(guessed_characters)

            # If the player reaches 0 health he lost.
            if number_of_lives == 0:
                is_game_over=True
                print("You lost.")
