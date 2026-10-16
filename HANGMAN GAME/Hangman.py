import random
import string
from Word_List import words

def get_valid_word(words):
    word = random.choice(words)
    # retry if the word contains a dash or a space
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed already

    # Game loop
    while len(word_letters) > 0:
        print("Letters guessed so far:", ' '.join(sorted(used_letters)))

        # THE CURRENT WORD
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('SONG TITLE:', ' '.join(word_list))

        user_input = input('Guess the R&B Song (single letter): ').upper()
        if len(user_input) != 1:
            print('Please enter a single character.')
            continue

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        elif user_input in used_letters:
            print('You have already used that character!')
        else:
            print('Invalid Character! Try Again.')

    print('\nCongratulations! You guessed the song:', word)


if __name__ == '__main__':
    hangman()