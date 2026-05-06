import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state."""

    # Show current snowman stage
    print(STAGES[mistakes])

    # Build word display
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())
    print("Guessed letters:", " ".join(guessed_letters))
    print()


def is_word_guessed(secret_word, guessed_letters):
    """ Checks if the whole word has been guessed. """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():
    """ Whole game functionality: Repeats until user found the word. """
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = []
    max_mistakes = len(STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!\n")
        else:
            print("Wrong!\n")
            mistakes += 1

        if is_word_guessed(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations! You saved the snowman! ☃️")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("Game over! The snowman melted.")
    print("The word was:", secret_word)



def main():
    play_game()


if __name__ == "__main__":
    main()