from datetime import datetime


def plan_activity():
    date_string = input("Enter a date (m/d/y): ")

    datetime_object = datetime.strptime(date_string, '%m/%d/%y')

    weather = input("Enter what weather we're having: ")

    activity = ""

    if datetime_object < datetime.now():
        print("That was so long ago! Who even remembers that?")

    if datetime_object >= datetime.now():
        if weather == "sunny" and datetime_object == datetime.now():
            print(f"Today is {date_string} and the weather is {weather}.")
            activity = "Let's go on a walk!"
        elif weather == "sunny" and datetime_object > datetime.now():
            print(f"The weather on {date_string} is sounds like a good day for a walk.")
            activity = "Let's plan a walk!"
        elif weather == "rainy" and datetime_object == datetime.now():
            activity = "I don't feel like going anywhere today!"
        elif weather == "rainy" and datetime_object > datetime.now():
            print(f"I heard {date_string} is going to be a rainy day.")
            activity = "Don't forget your umbrella!"

    print(activity)


    # print(f"Today is {date_string} and it's {weather}. We should {activity}!")

# Temperatuuriteisendaja ülesanne
def convert_temperatures():

    while True:
        end_unit = input("What units do you want to convert to? "
                      "Enter 'c' for Celsius, 'f' for Fahrenheit or 'k' for Kelvin: ")
        if end_unit != "c" and end_unit != "f" and end_unit != "k":
            print("Please choose Celsius, Fahrenheit or Kelvin.")
            continue
        else:
            break

    while True:
        start_unit = input("From what unit? "
                      "Enter 'c' for Celsius, 'f' for Fahrenheit or 'k' for Kelvin: ")
        if start_unit != "c" and start_unit != "f" and start_unit != "k":
            print("Please choose Celsius, Fahrenheit or Kelvin.")
            continue
        else:
            break

    if start_unit == "c":
        while True:
            try:
                celsius = float(input("Enter temperature in celsius: "))
            except ValueError:
                print("Please enter a numeral value.")
                continue
            else:
                break

        if end_unit == "f":
            fahrenheit = (celsius * 1.8) + 32
            print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
                  % (celsius, fahrenheit))

        elif end_unit == "k":
            kelvin = celsius + 273.15
            print('%.2f Celsius is equivalent to: %.2f Kelvin'
                  % (celsius, kelvin))

    elif start_unit == "f":
        while True:
            try:
                fahrenheit = float(input("Enter temperature in fahrenheit: "))
            except ValueError:
                print("Please enter a numeral value.")
                continue
            else:
                break

        if end_unit == "c":
            celsius = (fahrenheit - 32) / 1.8
            print('%.2f Fahrenheit is equivalent to: %.2f Celsius'
              % (fahrenheit, celsius))

        elif end_unit == "k":
            kelvin = 273.5 + ((fahrenheit - 32.0) * (5.0 / 9.0))
            print('%.2f Fahrenheit is equivalent to: %.2f Kelvin'
                  % (fahrenheit, kelvin))


    elif start_unit == "k":
        while True:
            try:
                kelvin = float(input("Enter temperature in Kelvin: "))
            except ValueError:
                print("Please enter a numeral value.")
                continue
            else:
                break

        if end_unit == "c":
            celsius = kelvin - 273.15
            print('%.2f Kelvin is equivalent to: %.2f Celsius'
              % (kelvin, celsius))

        elif end_unit == "f":
            fahrenheit = (9/5) * (kelvin - 273.15) + 32
            print('%.2f Kelvin is equivalent to: %.2f Fahrenheit'
                  % (kelvin, fahrenheit))


if __name__ == '__main__':
    # plan_activity()
    convert_temperatures()