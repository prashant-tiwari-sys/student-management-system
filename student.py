
from abc import ABC, abstractmethod

# Tuple: fixed grade boundaries
GRADE_SCALE = (
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F")
)


class Person(ABC):
    """Abstract base class."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_details(self):
        pass


class Student(Person):
    def __init__(self, student_id, name, age, course, marks):
        super().__init__(name)

        # Encapsulation: private student ID
        self.__student_id = str(student_id)
        self.age = int(age)
        self.course = course
        self.marks = marks

    @property
    def student_id(self):
        return self.__student_id

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        for minimum, grade in GRADE_SCALE:
            if average >= minimum:
                return grade

        return "F"

    def get_details(self):
        return (
            f"ID: {self.student_id} | Name: {self.name} | "
            f"Age: {self.age} | Course: {self.course} | "
            f"Average: {self.calculate_average():.2f} | "
            f"Grade: {self.calculate_grade()}"
        )


class ScholarshipStudent(Student):
    """Child class demonstrating inheritance and polymorphism."""

    def get_details(self):
        return super().get_details() + " | Scholarship: Eligible"
