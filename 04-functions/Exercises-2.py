"""Function examples."""


def func():
    # func()
    """Print statement when function is called."""
    print("I´m inside the function")


def my_name_is(name: str):
    # my_name_is(name)
    """Format a name as string from argument and print to console in a sentence."""
    print("My name is {name}".format(name=name))


def sum_six(num: int):
    # sum_six(num)
    """Print sum of int argument and 6."""
    return num + 6


def sum_numbers(a: int, b: int):
    # sum_numbers()
    """Print sum of two input integers."""
    return a + b


def usd_to_eur(usd: int):
    # usd_to_eur()
    """Convert input value in USD to EUR."""
    return usd * 0.8


if __name__ == '__main__':
    func()
    my_name_is("Bingus")
    print(sum_six(1))
    print(sum_numbers(1, 2))
    print(usd_to_eur(usd=100))
