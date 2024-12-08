import math


# Task 11
def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    # Write your code here
    originalSeconds = seconds
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds = originalSeconds
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."

# Task 12
def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    # Write your code here
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.radians(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."

# Task 13
def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = n * ("Hey")
    return lots_of_heys

# Task 14
def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    # Write your code here
    string_numbers = (str)(num_a) + (str)(num_b)
    return string_numbers

if __name__ == '__main__':
    print(time_converter(12345))
    print(student_helper(30))
    print(greetings(3))
    print(adding_numbers(123, 456))