"""Exercises from https://courses.cs.ut.ee/t/pythonkoolis/Main/KasuridaYl"""
import math


def greet(name: str):
    """Print greeting with name from argument."""
    print("Hello {name}".format(name=name))


def perform_math_operations():
    """
    Initial operation is 3 + 8 / (4 - 2) * 4.
    Return results of different variations of order of operations.
    """
    print(3 + 8 / (4 - 2) * 4)
    print((3 + 8 / (4 - 2)) * 4)
    print((3 + 8) / (4 - 2) * 4)


def kill_koll():
    """Print "killadi-koll" on every 3rd and 6th index, otherwise print "kill-koll"."""
    n = 1

    while n < 11:
        if n == 3 or n == 6:
            print("killadi-koll", end=" ")
            n = n + 1
        else:
            if n == 10:
                print("kill-koll")
            else:
                print("kill-koll", end=" ")
            n = n + 1


def print_song_lyrics():
    """Print each line of a popular nursery rhyme."""
    print("Rong see sõitis tsuhh tsuhh tsuhh,")
    print("piilupart oli rongijuht.")
    print("Rattad tegid rat tat taa,")
    print("rat tat taa ja tat tat taa.")
    print("Aga seal rongi peal,")
    print("kas sa tead, kes olid seal?")

    # Teise poole vastus: kuna muutustel pole otseseid korrelatsioone, saab sõnade väljavahetamist
    # teha manuaalselt. See omakorda põhjendab ka iga rea üksikult väljastamist.


def calculate_square_and_circle(radius: float):
    """
    Given radius is also 1/2 of square side.
    Calculate area and circumference of square; area and circumference of circle.
    """
    side = radius * 2
    square_area = round(side ** 2, 2)
    square_circumference = round(side * 4, 2)

    circle_area = round(math.pi * radius ** 2, 2)
    circle_circumference = round(2 * math.pi * radius, 2)

    print(f"Area of square: {square_area}")
    print(f"Circumference of square: {square_circumference}")
    print(f"Area of circle: {circle_area}")
    print(f"Circumference of circle: {circle_circumference}")


if __name__ == '__main__':
    kill_koll()
    calculate_square_and_circle(3.0)