"""Exercises from https://courses.cs.ut.ee/t/pythonkoolis/Main/SisendYl"""


# Ex. 1
def calculate_rectangle_circumference_and_area():
    a = float(input("Please enter length of side a: "))
    b = float(input("Please enter length of side b: "))

    circumference = 2 * (a + b)
    area = a * b

    #return circumference, area
    print(f"The circumference of the rectangle is {circumference}")
    print(f"The area of the rectangle is {area}")

# Ex. 2
def verify_age(age: int) -> str:
    if age > 18 or age < 7:
        return "You are not in the 7 to 18 age range."
    else:
        return "You are in the 7 to 18 age range."


def greet_by_age():
    # ask for name, age
    # verify age (if 7-18, greet based on boolean value) -> verifyAge(int age) -> returns str greeting
    # print greeting, print return value of verifyAge

    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    is_valid_age_format = age.isnumeric()

    # while not is_valid_age_format:
    #     print("This is not a valid format for age. Please enter an integer value.")
    #     age = int(input("Your age: "))  <-- todo Boolean value is not updated to True when valid type is entered.

    age_greeting = verify_age(int(age))

    print(f"Hello, {name}!")
    print(age_greeting)


# Ex. 3
def calculate_and_return_string(a: float, b: float, operator: str) -> str:
    """Perform calculation based on user input and return operation with result as string."""

    result = calculate(a, b, operator)

    if result is None:
        return "This is outside of my scope :("
    else:
        return f"{a} {operator} {b} = {result}"


def calculate(a: float, b: float, operator: str) -> float | None:
    """Determine type of operation from user input and perform calculation."""

    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return None


def take_user_input_and_calculate_result():
    """Ask and verify user input and call method to perform required calculation."""

    a = input("Please enter first number: ")
    while not a.isnumeric():
        print("Please enter a valid number: ")
        a = input()

    b = input("Please enter second number: ")
    while not b.isnumeric():
        print("Please enter a valid number: ")
        b = input()

    a = int(a)
    b = int(b)
    operator = input("Please enter operator symbol: ")
    result = calculate_and_return_string(a, b, operator)

    print(result)


# Ex. 4
def calculate_frequency(a: int, b: int, operator: str) -> int:
    pass

def display_barks_n_times():
    frequency = calculate_frequency()


if __name__ == '__main__':
    # calculate_rectangle_circumference_and_area()
    # greet_by_age()
    take_user_input_and_calculate_result()