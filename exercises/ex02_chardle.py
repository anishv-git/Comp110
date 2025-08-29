"""Chardle - A cute step toward Wordle."""

__author__ = "730773852"


def input_word() -> str:
    """Prompt the user to enter a 5-character word."""
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """Prompt the user to enter a single character."""
    character = input("Enter a single character: ")
    if len(character) != 1:
        print("Error: Character must be a single character.")
        exit()
    return character


def contains_char(word: str, letter: str) -> None:

    print("Searching for " + letter + " in " + word)

    # helps keep track of instances
    count = 0

    # Takes in the the index of every character in the word to see if it matches the letter

    if len(word) > 0 and word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1

    if len(word) > 1 and word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1

    if len(word) > 2 and word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1

    if len(word) > 3 and word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1

    if len(word) > 4 and word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1

    # helps in assessing the total count/instances of a certain character in a word
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
