"""Tests for solution."""
from solution import students_study, lottery, fruit_order
import pytest


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False
    assert students_study(1, True) is False
    assert students_study(2, True) is False
    assert students_study(4, True) is False


def test__students_study__night_without_coffee__no_studying():
    """During night without coffee students do not study."""
    assert students_study(3, False) is False
    assert students_study(1, False) is False
    assert students_study(2, False) is False
    assert students_study(4, False) is False


def test_students_study__day_coffee__studying():
    """During the day with coffee students study."""
    assert students_study(5, True) is True
    assert students_study(13, True) is True
    assert students_study(17, True) is True


def test__students_study__day_without_coffee__no_studying():
    """During the day without coffee students do not study."""
    assert students_study(5, False) is False
    assert students_study(13, False) is False
    assert students_study(17, False) is False


def test__students_study__evening_with_coffee__studying():
    """In the evening without coffee students study."""
    assert students_study(18, True) is True
    assert students_study(20, True) is True
    assert students_study(24, True) is True


def test__students_study__evening_without_coffee__studying():
    """In the evening without coffee students study."""
    assert students_study(18, False) is True
    assert students_study(20, False) is True
    assert students_study(24, False) is True


def test_fruit_order__large_baskets_equal_to_total_kg():
    """Big baskets weight is equal to total ordered amount. Therefore, 0 small baskets are returned."""
    assert fruit_order(5, 2,  10) == 0
    assert fruit_order(2, 3, 15) == 0
    assert fruit_order(9, 400, 2000) == 0
    assert fruit_order(0, 2, 10) == 0


def test_fruit_order__big_baskets_less_than_total_kg():
    """Big baskets weight is less than total ordered amount, therefore n small baskets are returned."""
    assert fruit_order(10, 1, 10) == 5
    assert fruit_order(0, 2, 30) == -1
    assert fruit_order(7, 2, 60) == -1
    assert fruit_order(1000, 200, 2000) == 1000
    assert fruit_order(2, 2, 7) == 2


def test_fruit_order__big_baskets_weight_more_than_total_kg():
    """Big baskets weight is greater than total ordered amount."""
    assert fruit_order(10, 3, 10) == 0
    assert fruit_order(0, 6, 4)  == -1
    assert fruit_order(100, 402, 2000) == 0
    assert fruit_order(100, 404, 2001) == 1
    assert fruit_order(1000, 1000, 4000) == 0
    assert fruit_order(3, 1001, 4004) == -1
    assert fruit_order(0, 10, 80) == -1
    assert fruit_order(0, 6, 25) == 0


def test_fruit_order__no_big_baskets():
    """0 big baskets are available."""
    assert fruit_order(0, 0, 20) == -1
    assert fruit_order(16, 0, 16) == 16
    assert fruit_order(2000, 0, 2000) == 2000
    assert fruit_order(6, 0, 7) == -1
    assert fruit_order(6, 0, 5) == 5


def test_fruit_order__zero_kg_ordered():
    """Total ordered amount is 0kg."""
    assert fruit_order(1, 1, 0) == 0
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(1, 0, 0) == 0
    assert fruit_order(0, 1, 0) == 0


def test_lottery_winning_numbers():
    """If all numbers are 5, return max winning number 10.
    If all numbers are equal but not 5, return 5."""
    assert lottery(5, 5, 5) == 10
    assert lottery(2, 2, 2) == 5
    assert lottery(1, 1, 1) == 5
    assert lottery(-1, -1, -1) == 5
    assert lottery(0, 0, 0) == 5


def test_lottery__a_is_not_b_or_c():
    """If a != b or a != c, return 1."""
    assert lottery(1, 3, 3) == 1
    assert lottery(2, 1, 4) == 1


def test_c_only_equals_b():
    """If b is equal to a and c is not equal to a, return 0."""
    assert lottery(1, 1, 2) == 0
    assert lottery(1, 2, 1) == 0