"""Function examples."""


# func()
def func():
    print("I´m inside the function")

# my_name_is(name)
def my_name_is(name: str):
    print("My name is {name}".format(name=name))


# sum_six(num)`
def sum_six(num: int):
    return num + 6


# sum_numbers()
def sum_numbers(a: int, b: int):
    return a + b


# usd_to_eur()
def usd_to_eur(usd: int):
    return usd * 0.8


if __name__ == '__main__':
    func()
    my_name_is("Bingus")
    print(sum_six(1))
    print(sum_numbers(1, 2))
    print(usd_to_eur(usd=100))