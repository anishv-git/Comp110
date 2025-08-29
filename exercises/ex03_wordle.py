"""Wordle - a word guessing game"""

__author__ = "730773852"


def input_guess(secret_word_len: int) -> str:
    """Prompts the user to input a guess of the expected length."""

    guess = input(f"Enter a {secret_word_len} character word: ")

    # While true it will return the guess
    while len(guess) != secret_word_len:
        print(f"That wasn't {secret_word_len} chars! Try again.")
        guess = input(f"Enter a {secret_word_len} character word: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if a single character is present in the given word."""
    assert len(char_guess) == 1, "The second parameter must be a single character."
    return char_guess in secret_word


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis representing the accuracy of the guess."""

    if len(guess) != len(secret):
        print("Error: The guess and secret word must be of the same length.")
        return ""

    # The emoji assignment for each color
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_result = ""
    index = 0

    # checks for whether the characters in guess match secret word
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX

        index += 1

    return emoji_result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turns = 6
    turn_num = 1

    while turn_num <= turns:
        print(f"=== Turn {turn_num}/{turns} ===")
        guess = input_guess(
            len(secret)
        )  # Prompt the user for a guess of the correct length.

        # Compare the guess to the secret and print the emoji results.
        emoji_result = emojified(guess, secret)
        print(emoji_result)

        # Check if the user has won.
        if guess == secret:
            print(f"You won in {turn_num}/{turns} turns!")
            return

        turn_num += 1

    # If the loop ends without a win:
    print(f"X/{turns} - Sorry, try again tomorrow!")


# This line allows the game to run when the script is executed.
if __name__ == "__main__":
    main(secret="china")
