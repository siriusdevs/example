"""Just a few exceptions for my little project."""
from datetime import date


class Removed(Exception):
    """Exception used for expelled students."""

    def __init__(self, cur_date: date, student: str, message: str = "No such student!"):
        """Creates a custom exception.

        Args:
            cur_date : datetime.date - the date of the day when the exception occured.
            student : str - the name of the student.
            message : str - the message of the exception.
        """
        self.cur_date = cur_date
        self.message = message
        self.student = student
        super().__init__(self.message)

    def __str__(self):
        """Returns string representation of an object."""
        return '{0}, {1} -> {2}'.format(self.cur_date, self.student, self.message)
