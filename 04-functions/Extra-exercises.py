"""Extra function exercises"""


# Banner exercise
def banner(slogan: str):
    """Return uppercase version of entered string value."""
    return str.upper(slogan)


def show_banner():
    """
    Print slogan based on user input.
    User is asked to input the slogan and nr of times it should be repeated. The method for returning
    slogan as uppercase is then called and the returned result is printed to console the input nr of times.
    """
    num_of_repeats = input("How many times do you want to repeat your slogan? Enter: ")
    slogan_input = input("Please enter your slogan: ") + ' '

    print(banner(slogan_input) * int(num_of_repeats))

# Party budget exercise
def eelarve(num_of_guests: int):
    return 10 * num_of_guests + 55

def calculate_min_and_max_budget():
    num_of_invited_guests = input("Mitu inimest on peole kutsutud? ")
    num_of_guests_coming = input("Mitu inimest tuleb? ")

    max_budget = eelarve(int(num_of_invited_guests))
    min_budget = eelarve(int(num_of_guests_coming))

    print(f"Maksimaalne eelarve on {max_budget} eurot")
    print(f"Minimaalne eelarve on {min_budget} eurot")

if __name__ == '__main__':
        # show_banner()
    calculate_min_and_max_budget()


