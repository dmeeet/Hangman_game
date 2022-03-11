import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    alphabet = ["a b c d e f g h i g k l m n o p q r s t  u v w x y z"]
    dash = "-"
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play!")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')

    while not guessed and tries > 0:
        guess = input("Please guess a latter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                print(guessed_letters)
            elif guess not in word:
                print("is not in the word")
                tries -= 1
                guessed_letters.append(guess)
                print(guessed_letters)
            else:
                print("Good,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not valid guess')
        print(display_hangman(tries))
        print(word_completion)
        print(guessed_letters)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,

        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,

        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,

        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Enter 'Y' if you want to restart the game:").upper() == "Y":
        word = get_word()
        play(word)
    else:
        print("GOODBYE!")


if __name__ == '__main__':
    main()
