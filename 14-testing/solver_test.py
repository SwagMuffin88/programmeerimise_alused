import pytest
from solver import quadratic_solution

# @pytest.fixture()
# def test_base_arguments():
#     assert -1 in quadratic_solution(5, 6, 1)


@pytest.fixture()
def setup():
    print("\n Test starting...")
    yield
    print("\n Test finished.")

@pytest.mark.usefixtures("setup")
class TestQuadraticSolver:
    def test_solve_normal_values(self):
        assert quadratic_solution(1, -3, 2) == (1, 2)

    def test_solve_float_values(self):
        assert quadratic_solution(1, -4, 3.75) == (1.5, 2.5)

    def test_solve_one_solution(self):
        assert quadratic_solution(1, -4, 4) == (2, )

    def test_solve_no_solutions(self):
        assert quadratic_solution(1, 1, 1) is None

    def test_solve_linear_equation(self):
        assert quadratic_solution(0, 1, 1) == (-1, )
