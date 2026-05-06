import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """ Choose random word from WORDS """
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """ Improved display output """

    print("\n" + "=" * 30)
    print(STAGES[mistakes])

    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in secret_word]
    )

    print("Word:       ", display_word)
    print("Guessed:    ", " ".join(sorted(guessed_letters)))
    print("Mistakes:   ", mistakes, "/", len(STAGES) - 1)
    print("=" * 30 + "\n")


def is_word_guessed(secret_word, guessed_letters):
    """ Returns true if secret word is in guessed letter, else false """
    return all(letter in guessed_letters for letter in secret_word)


def get_valid_input(guessed_letters):
    """ Handles clean input validation """
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly ONE letter!\n")
            continue

        if guess in guessed_letters:
            print("Already guessed.\n")
            continue

        return guess


def play_game():
    """ Game functionality """
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    max_mistakes = len(STAGES) - 1

    print("\n *** Welcome to Snowman Meltdown! ***\n")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_input(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(" Correct!\n")
        else:
            print(" Wrong!\n")
            mistakes += 1

        if is_word_guessed(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("  You saved the snowman!\n")
            return True

    display_game_state(mistakes, secret_word, guessed_letters)
    print("  The snowman melted...")
    print("The word was:", secret_word, "\n")
    return False


def ask_replay():
    """Replay prompt"""
    while True:
        choice = input("Play again? (y/n): ").lower().strip()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        print("Please enter y or n.\n")


def main():
    """ Main function """
    while True:
        play_game()
        if not ask_replay():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()