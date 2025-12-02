"""Extra function exercises"""


# Electricity bill exercise
def convert_price_from_cent_to_eur(price_s_kw: float) -> float:
    """
    Convert electricity price from s/kWh to €/MWh.
    """
    #price_in_eur = price_s_kw / 100 -> can be simplified
    return price_s_kw * 10

def elektrihind():
    """
    Convert price from user input and display result.
    User is asked to enter electricity price in s/kWh and the price is then converted to €/MWh.
    """
    price_s_kw = float(input("Sisesta elektrihind sentides kilovatt-tunni kohta: "))
    price_m_mw = convert_price_from_cent_to_eur(price_s_kw)

    print(f"{price_s_kw} s/kWh on {price_m_mw} €/MWh")


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
    """
    Calculate expected budget based on number of guests.
    The input is multiplied by the expense per guest and added to the room rent price.
    """
    return 10 * num_of_guests + 55

def calculate_min_and_max_budget():
    """Calculate max and min expected party budget based on user input."""
    num_of_invited_guests = input("Mitu inimest on peole kutsutud? ")
    num_of_guests_coming = input("Mitu inimest tuleb? ")

    max_budget = eelarve(int(num_of_invited_guests))
    min_budget = eelarve(int(num_of_guests_coming))

    print(f"Maksimaalne eelarve on {max_budget} eurot")
    print(f"Minimaalne eelarve on {min_budget} eurot")

if __name__ == '__main__':
    elektrihind()

