"""School class which stores information about courses and students."""
from __future__ import annotations
from typing import TYPE_CHECKING

# Prevent circular imports during runtime
if TYPE_CHECKING:
    from student import Student
    from course import Course


class School:
    """School class."""

    def __init__(self, name: str):
        """School constructor."""
        self.name = name
        self.student: list["Student"] = []
        self.courses: list["Course"] = []
        # Store grades as (Student, Course, Grade) or similar if needed
        self.student_grades: list[tuple["Student", "Course", int]] = []

    def add_course(self, course: "Course"):
        """Add a course to the school."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: "Student"):
        """Add a student to the school and assign an ID if not already set."""
        if student not in self.student:
            if student.get_id() is None:
                student.set_id(len(self.student) + 1)
            self.student.append(student)

    def add_student_grade(self, student: "Student", course: "Course", grade: int):
        """Add a grade to a student for a specific course."""
        if student in self.student and course in self.courses:
            # 1. Add to the School's log
            self.student_grades.append((student, course, grade))

            # 2. Add to the Student's personal list (for student.get_average_grade)
            student.grades.append((course, grade))

            # 3. Add to the Course's list (for course.get_average_grade)
            course.student_grades.append((student, grade))

    def get_students(self) -> list["Student"]:
        """Get all students in the school."""
        return self.student

    def get_courses(self) -> list["Course"]:
        """Get all courses in the school."""
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list["Student"]:
        """Return students ordered by average grade descending (highest first)."""
        return sorted(
            self.student,
            key=lambda s: s.get_average_grade(),
            reverse=True
        )