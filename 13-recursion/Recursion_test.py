import pytest
from Exercises import sum_digits_recursive
import sys


@pytest.fixture()
def setup():
    # Change max nr of str digits in int conversion for a recursive method.
    sys.set_int_max_str_digits(5000)
    print("\n Test starting...")
    yield
    print("\n Test finished.")


@pytest.mark.usefixtures("setup")
class TestRecursive:
    def test_5000_digit_input(self):
        assert sum_digits_recursive(int("1" * 999)) == 999