import random

WORDS = ["python", "git", "github", "snowman", "meltdown"]

STAGES = [
    # Stage 0: Full snowman
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2: Only the head remains
    """
     ___  
    /___\\ 
    (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
     ___  
    /___\\ 
    """
]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state."""

    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())
    print("Guessed letters:", " ".join(guessed_letters))
    print()


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected:", secret_word)  # Debug (later entfernen)

    mistakes = 0
    guessed_letters = []

    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess:
            guessed_letters.append(guess)
            if not guess in secret_word:
                mistakes += 1

    # Final state
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Game over! The snowman has melted.")


def main():
    play_game()


if __name__ == "__main__":
    main()