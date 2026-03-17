import math


def quadratic_solution(a, b, c):
    """Solve quadratic equation."""
    if a == 0:
        return - (c / b),
    disc = b**2 - 4 * a * c
    if disc < 0:
        return None

    if disc == 0:
        return -b / (2 * a),

    x1 = (-b - math.sqrt(disc)) / (2 * a)
    x2 = (-b + math.sqrt(disc)) / (2 * a)

    return x1, x2