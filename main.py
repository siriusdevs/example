"""Main module uses all others, meant to be run."""
from datetime import date
from exceptions import Removed
from random import choice, randint
from string import ascii_letters, ascii_uppercase, digits
from student import Student
from typing import List


group = ['Bezborodov', 'Vechernina', 'Vylkov', 'Gafiyatullina', 'Filatov',\
         'Gotskina', 'Kulgavykh', 'Medvedenko', 'Nazarov', 'Nesterov',\
         'Orekhov', 'Prikhodko', 'Pruzhinin', 'Smirnov', 'Snopov', 'Shutova'
         ]
YEAR, MONTH, DAY = 2023, 1, 20
THE_DATE = date(YEAR, MONTH, DAY)


def make_up_task(student: Student, starred: bool = None) -> str:
    """Makes up a string task. Yells if the task is starred. Contains digits only if is meant for Maxim.

    Args:
        student : Student - student, who will get the task.
        starred : bool - indicates if the task is marked with star.

    Returns: str - made up task from random symbols.
    """
    if starred:
        alph = ascii_uppercase
    elif student.name == 'Bezborodov':
        alph = digits
    else:
        alph = ascii_letters
    return ''.join([choice(alph) for _ in range(100)])


def give_tasks(student: Student, num: int = 5) -> None:
    """Gives tasks to the student, default number of tasks is five.

    Args:
        student : Student - student, who will get the task.
        num : int - the number of tasks, defaults to five.
    """
    tasks = [make_up_task(student) for _ in range(num)]
    student.tasks = tasks


def work(cur_date: date, students: List[Student]) -> None:
    """Works for the day. Gives tasks to students, checks if they exist.

    Args:
        cur_date : datetime.date - the date of the day.
        students : List[Student] - the list of students that we have.

    Raises:
        Removed : if student doesn't exist.
    """
    for student in students:
        if not (student.name == 'Nazarov' and cur_date > THE_DATE):
            give_tasks(student, randint(1, 5))
        else:
            raise Removed(cur_date=cur_date, student=student.name)


if __name__ == '__main__':
    work(date.today(), [Student(name) for name in group])
