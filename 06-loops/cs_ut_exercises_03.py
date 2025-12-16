"""https://courses.cs.ut.ee/t/pythonkoolis/Main/TsykkelYl"""


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


if __name__ == '__main__':
    #greet_user()
    # add_ten_numbers_from_user_and_add_all()
    # add_numbers_while_loop_ver()
    add_numbers_keystroke_ver()