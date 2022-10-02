"""Module used for testing main functions."""
from datetime import date
from exceptions import Removed
from main import make_up_task, give_tasks, work
from student import Student
import pytest


def test_make_up_usual():
    """Tests casual tasks."""
    assert make_up_task(Student('Gotskina')).isalpha()


def test_make_up_starred():
    """Tests starred tasks."""
    assert make_up_task(Student('Nazarov'), starred=True).isupper()


def test_make_up_for_bezborodov():
    """Tests Maxim's tasks."""
    assert make_up_task(Student('Bezborodov')).isdigit()


def test_giving_tasks():
    """Tests if number of student's tasks increases when given some."""
    num = 5
    student = Student('Nesterov')
    give_tasks(student, num)
    assert len(student.tasks) == num


normal_dates = (2022, 10, 20), (2022, 11, 20)
work_tests = [(date(*normal_dates[0]), Student('Gotskina')), (date(*normal_dates[1]), Student('Prihodko'))]


@pytest.mark.parametrize('work_date, student', work_tests)
def test_work(work_date: date, student: Student):
    """Tests if working also increases the number of student's tasks."""
    init_num_tasks = len(student.tasks)
    work(work_date, [student])
    assert len(student.tasks) > init_num_tasks


def test_work_raises():
    """Tests if works with expelled students."""
    normal = 2023, 1, 23
    work_date = date(*normal)
    student = Student('Nazarov')
    with pytest.raises(Removed) as exc:
        work(work_date, [student])
        assert str(exc)
