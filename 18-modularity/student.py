"""Student class with student name and grades."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from course import Course


class Student:
    """Student class, do not change."""

    def __init__(self, name: str):
        """Student constructor."""
        self.name = name
        self.id = None
        self.grades: list[tuple["Course", int]] = []

    def set_id(self, id: int):
        """Set student id."""
        if self.id is not None:
            return
        else:
            self.id = id

    def get_id(self) -> int:
        """Return student id."""
        return self.id

    def get_grades(self) -> list[tuple[Course, int]]:
        """Return student grades."""
        return self.grades

    def get_average_grade(self) -> float:
       """Return student average grade."""
       if not self.grades:
           return -1.0

       total_sum = sum(grade for course, grade in self.grades)
       return total_sum / len(self.grades)

    def __repr__(self) -> str:
        """Return string representation of a student."""
        return self.name