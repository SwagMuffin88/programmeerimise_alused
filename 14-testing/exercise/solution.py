"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    Kui on õhtupoolne ja öine aeg (vahemikus kl 18 kuni kl 24, otspunktid kaasa arvatud),
        sel juhul kohvi joomine ei ole oluline

    Kui on hommikupoolne ja lõuna aeg (vahemikus kl 5 kuni 17 otspunktid kaasa arvatud),
        sel juhul kohvi joomine on äärmselt tähtis

    Vahemikus kl 1 kuni 4 (otspunktid kaasa arvatud) tublid tudengid ei õpi, vaid magavad :)


    """
    if 18 <= time <= 24:
        return True

    elif 5 <= time <= 17:
        match coffee_needed:
            case True:
                return True
            case False:
                return False

    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10

    else:
        if a == b and c == a:
            return 5
        elif a != b and a != c:
            return 1
    return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    max_big_baskets = ordered_amount // 5
    used_big = min(big_baskets, max_big_baskets)

    remaining_amount = ordered_amount - (used_big * 5)

    if remaining_amount <= small_baskets:
        return remaining_amount
    else:
        return -1


if __name__ == '__main__':
    # print(lottery(2, 1, 1))
    print(fruit_order(7, 1, 10))
    # print(fruit_order(4, 1, 9))

    # print(students_study(24, False))
    # print(students_study(1, True))
    # print(students_study(10, False))