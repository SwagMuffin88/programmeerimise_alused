"""https://courses.cs.ut.ee/t/pythonkoolis/Main/TsykkelYl"""
from datetime import timedelta
from random import randint
import datetime


# Ex. 1
def greet_user():
    name = input("Palun sisesta oma nimi: ")

    for i in range(5):
        print(f"Tere, {name}, {i + 1}. korda!")


# Ex. 2
def add_ten_numbers_from_user_and_add_all():
    total = 0
    for i in range(10):
        number = int(input(f"Palun sisesta {i + 1}. arv: "))
        total += number

    print(total)


def add_numbers_while_loop_ver():
    total = 0
    n = 1
    while n <= 10:
        number = float(input(f"Palun sisesta {n}. arv: "))
        total += number
        n += 1

    print(total)


def add_numbers_keystroke_ver():
    total = 0
    n = 1

    while True:
        user_input = input(f"Palun sisesta {n}. arv: ")
        if not user_input.isnumeric() or user_input == "":
            break

        number = float(user_input)
        total += number
        n += 1

    print(total)

# Ex.3
def create_addition_problem(min_value, max_value):
    # Create addition problems with random integers.

    a = randint(min_value, max_value)
    b = randint(min_value, max_value)
    return f"{a} + {b}"

def calculate_correct_answer(problem:str) -> int:
    parts = problem.split() # Also includes operator, so it is possible to widen scope to other operations
    numbers = [int(part) for part in parts if part.isdigit()]

    a = int(numbers[0])
    b = int(numbers[1])
    return a + b

def is_correct_answer(answer: int, problem: str) -> bool:
    correct_answer = calculate_correct_answer(problem)
    return answer == correct_answer

def test_user_math_skills():
    """Ask for number range, create 10 random addition problems and check every answer from user input."""

    print("This is a math test. You will see 10 addition problems.")
    print("Please enter a range for problem range: ")
    min = int(input("Min value: "))
    max = int(input("Max value: "))
    incorrect_count = 0

    print("Here are your math problems: ")

    for i in range(10):
        math_problem = create_addition_problem(min, max)
        print(math_problem)

        user_answer = int(input("Enter your answer: "))
        is_correct = is_correct_answer(user_answer, math_problem)
        incorrect_count = 0

        if is_correct:
            print("That is correct!")
        else:
            incorrect_count += 1
            print("That is unfortunately not correct.")

    score = 10 - incorrect_count
    print("You have completed the mini math test.")
    print(f"Your score is: {score}/10")

# Ex. 4 + 5
def create_random_and_compare_to_user():
    print("Guess a number between 1 and 20.")
    number = randint(1, 20)
    try_count = 0

    #while True:
    # for i in range(5):
    while try_count < 5:
        try_count += 1
        user_number = int(input("Try to guess it: "))

        if user_number < number:
            print("That is a bit small.")
        elif user_number > number:
            print("That is a bit too much.")
        elif user_number == number:
            print("That's right!")
            break
    else:
        print(f"The correct number was {number}.")

    print(f"Your test has ended. You tried {try_count} times.")


# Ex. 6
def print_table_of_number_combinations():
    """Print every possible combination of numbers in layout x - y - z where each number is 1 to 20."""

    count = 0
    for z in range(1, 21):
        for y in range(1, 21):
            for x in range(1, 21):
                count += 1
                print(f"{z} - {y} - {x}")

    print(f"Generated {count} total combinations.")


def print_grid(size:int, alt: str, symbol: str):
    for col in range(size):
        for row in range(size):
            if row == col or row + col == size - 1:
                print(f"{alt}", end=" ")
            else:
                print(f"{symbol}", end=" ")
        print()


# Ex 8
def convert_time(time: timedelta) -> str:
    if time < datetime.timedelta(hours=1):
        time_minutes = round(time.total_seconds() / 60, 0)
        return f"Your travelling time is {time_minutes} min."
    else:
        time_hours = round(time.total_seconds() / 3600, 2)
        return f"Your travelling time is {time_hours} h."


def calculate_time_difference(old_time: int | timedelta, time: timedelta) -> str:
    difference = old_time - time

    if old_time < time:
        return f"Your new speed added extra {abs(round(difference.total_seconds() / 60, 0))} minutes."
    elif time < old_time:
        return f"Your new speed saved you {round(difference.total_seconds() / 60, 0)} minutes."
    else:
        return f"There was no difference in time."


def calculate_speed_difference():
    """Calculate the time it takes to travel through given distance at different speeds and compare the differences."""

    # Kui v = L / t, siis t = L / v
    # distance = userinput(enter your distance) -> muutumatu
    # speed = userinput(enter your speed) -> muutuv
    # loop while input is not empty string
    # output for incorrect input (permit only numeral values)

    distance = float(input("Please enter your distance in km: "))
    speed = input("Please enter your speed in km/h: ")
    old_time = -1

    while speed != "":
        if speed.isnumeric():
            time = datetime.timedelta(hours=distance / float(speed))

            time_converted_result = convert_time(time)
            print(time_converted_result)

            if old_time != -1:
                difference_result = calculate_time_difference(old_time, time)
                print(difference_result)

            speed = input("Please enter a new speed in km/h: ")
            old_time = time
        else:
            print("Please enter a numeric value for your speed.")
            speed = input("Please enter your speed in km/h: ")


# Ex. 9

DICE_ART = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

def throw_dice():
    dice_counter = 0
    die_height = len(DICE_ART[1])
    die_face_separator = " "

    while dice_counter < 3:
        dice_value = randint(1, 6)
        dice_faces = [DICE_ART[dice_value]]

        dice_faces_rows = []
        for row in range(die_height):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row])
            row_string = die_face_separator.join(row_components)
            dice_faces_rows.append(row_string)

        dice_faces_diagram = "\n".join(dice_faces_rows)
        print(dice_faces_diagram)
        dice_counter += 1


def play_dice_as_user():
    check = ""
    while check != "n":
        name = input("Enter your name: ")
        print(f"The current player is {name}")
        throws = int(input("Please enter the number of throws you wish to have (1-3):"))
        count = 0

        while count < throws:
            print(f"Round {count + 1}")
            throw_dice()
            count += 1

        print(f"{name}'s round is up!")
        check = input("Would anyone else like to play? (y/n): ").lower()

if __name__ == '__main__':
    #test_user_math_skills()
    #create_random_and_compare_to_user()
    #print_table_of_number_combinations()
    #print_grid(6, "x", "o")
    #calculate_speed_difference()
    play_dice_as_user()