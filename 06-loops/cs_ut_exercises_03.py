"""https://courses.cs.ut.ee/t/pythonkoolis/Main/TsykkelYl"""
from random import randint

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

    for i in range(9):
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

# Ex. 4
def create_random_and_compare_to_user():
    print("Guess a number between 1 and 20.")
    number = randint(1, 20)

    while True:
        user_number = int(input("Try to guess it: "))
        if user_number < number:
            print("That is a bit small. Try again.")
        elif user_number > number:
            print("That is a bit too much. Try again.")
        else:
            print("That's right!")
            break


if __name__ == '__main__':
    #test_user_math_skills()
    create_random_and_compare_to_user()