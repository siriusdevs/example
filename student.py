"""Module for defining Student class and some excess classes."""
from random import randint
from typing import List


class Being:
    """Defines all beings."""

    def __init__(self, age: int, name: str):
        """Creates a being.

        Args:
            age : int - the age of a being.
            name : str - the name of a being.
        """
        self.name = name
        self.age = age


class Person(Being):
    """Defines all persons."""

    def __init__(self, age: int, name: str, occupation: str):
        """Creates a person.

        Args:
            age : int - the age of a being. Age defaults to 18.
            name : str - the name of a being.
            occupation : str - a place of living.
        """
        super().__init__(age, name)
        self.occupation = occupation


class Student(Being):
    """Defines some students."""

    def __init__(self, name: str, age: int = 18):
        """Creates a student.

        Args:
            age : int - the age of a being. Age defaults to 18.
            name : str - the name of a being.
        """
        super().__init__(age, name)
        self.name = name
        self.laziness = randint(9, 10)
        self.__tasks = []

    @property
    def tasks(self):
        """Tasks property."""
        return self.__tasks

    @tasks.setter
    def tasks(self, new_tasks: List[str]):
        """Tasks setter.

        Args:
            new_tasks: List[str] - the list of string tasks.
        """
        self.__tasks = new_tasks
