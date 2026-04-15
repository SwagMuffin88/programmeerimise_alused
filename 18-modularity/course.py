"""Course class with name and grades."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student


class Course:
    """Course class, do not change."""

    def __init__(self, name: str):
        """Course constructor."""
        self.name = name
        self.student_grades: list[tuple["Student", int]] = []

    def get_grades(self) -> list[tuple["Student", int]]:
        """Get all grades of a course."""
        return self.student_grades

    def get_average_grade(self) -> float:
        """Get average grade of a course."""
        if not self.student_grades:
            return -1.0

        total_sum = sum(grade for student, grade in self.student_grades)
        return total_sum / len(self.student_grades)

    def __repr__(self):
        """Return string representation of a course."""
        return self.name