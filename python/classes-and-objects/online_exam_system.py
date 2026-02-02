"""
Problem Statement:
Design a Python program to manage an online examination system using classes
and objects. The system should manage questions, students, and exam attempts.
Each question should store question text, correct answer, and marks. Each
student should store student ID and name. An exam attempt should associate a
student with multiple questions, record answers given by the student, evaluate
the answers, and calculate the total score. The program should accept details
from the user and display the final score for each student.
"""

class Question:
    def __init__(self, question_text, correct_answer, marks):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.marks = marks


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class ExamAttempt:
    def __init__(self, student):
        self.student = student
        self.answers = []
        self.score = 0

    def answer_question(self, question, given_answer):
        self.answers.append((question, given_answer))

    def evaluate(self):
        total = 0
        for question, answer in self.answers:
            if answer.lower() == question.correct_answer.lower():
                total += question.marks
        self.score = total

    def get_score(self):
        return self.score


questions = []
students = []
attempts = []

q_count = int(input("Enter number of questions: "))

for i in range(q_count):
    print(f"\nQuestion {i + 1}")
    text = input("Enter question text: ")
    correct = input("Enter correct answer: ")
    marks = int(input("Enter marks: "))
    questions.append(Question(text, correct, marks))


s_count = int(input("\nEnter number of students: "))

for i in range(s_count):
    print(f"\nStudent {i + 1}")
    sid = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    students.append(Student(sid, name))


for student in students:
    print(f"\nExam for {student.name}")
    attempt = ExamAttempt(student)

    for question in questions:
        print("Question:", question.question_text)
        ans = input("Enter answer: ")
        attempt.answer_question(question, ans)

    attempt.evaluate()
    attempts.append(attempt)


print("\n--- Exam Results ---")
for attempt in attempts:
    print("\nStudent ID:", attempt.student.student_id)
    print("Student Name:", attempt.student.name)
    print("Final Score:", attempt.get_score())


"""
Sample Output:

Enter number of questions: 2

Question 1
Enter question text: Capital of France
Enter correct answer: Paris
Enter marks: 5

Question 2
Enter question text: 2 + 2
Enter correct answer: 4
Enter marks: 5

Enter number of students: 1

Student 1
Enter student ID: 101
Enter student name: Rahul

Exam for Rahul
Question: Capital of France
Enter answer: Paris
Question: 2 + 2
Enter answer: 4

--- Exam Results ---

Student ID: 101
Student Name: Rahul
Final Score: 10
"""
