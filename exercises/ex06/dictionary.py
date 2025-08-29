"""Exercise 06 - Dictionay Utility Functions"""

__author__ = "730773852"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverses the value of key to the value of the value"""

    inverse_dict: dict[str, str] = {}

    for key in dict1:
        value = dict1[key]
        if value in inverse_dict:
            raise KeyError(
                f"Duplicate value found for key '{key}' with value '{value}'"
            )
        inverse_dict[value] = key
    return inverse_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Shows which color shows up the most in a dict"""
    if colors == {}:  # Check if the dictionary is empty
        return ""  # Return an empty string for an empty dictionary

    color_count: dict[str, int] = {}  # Dictionary to count occurrences of each color
    order: list[str] = []  # List to keep track of the order of first appearances

    # Count occurrences of each color and track the order
    for name in colors:
        color: str = colors[name]  # Get the corresponding color
        if color not in color_count:
            color_count[color] = 0
            order.append(color)  # Store the order of appearance
        color_count[color] += 1

    # Find the most frequent color, respecting order of appearance
    most_popular: str = order[0]  # Initialize with the first color in order
    max_count: int = color_count[most_popular]  # Get the initial count

    for color in order:
        if color_count[color] > max_count:
            most_popular = color
            max_count = color_count[color]

    return most_popular


def count(list: list[str]) -> dict[str, int]:
    """Returns the fequency of a word in a list"""

    result: dict[str, int] = {}

    for item in list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Grouping words by their initial letters"""
    result: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()

        if first_letter not in result:
            result[first_letter] = []

        result[first_letter].append(word)

    return result


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates the attendance log for a specific day by adding a student"""
    if day in attendance_log:
        if student not in attendance_log[day]:  # Only add if not already present
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]  # Create a new list if the day is not present
