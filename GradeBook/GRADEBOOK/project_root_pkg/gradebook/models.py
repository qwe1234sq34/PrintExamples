
"""Student / GradeBook 클래스 정의"""
from .utils import mean, letter_grade

class Student:
    def __init__(self, name, scores):
        self.name = name
        # scores: list of numbers
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

    def __repr__(self):
        return f"Student(name={self.name!r}, avg={self.average():.2f}, grade={self.grade()})"

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0.0
        return mean([s.average() for s in self.students])

    def grade_distribution(self):
        dist = {"A":0,"B":0,"C":0,"D":0,"F":0}
        for s in self.students:
            g = s.grade()
            dist[g] = dist.get(g,0) + 1
        return dist

    def __len__(self):
        return len(self.students)

    def __repr__(self):
        return f"GradeBook({len(self.students)} students)"
