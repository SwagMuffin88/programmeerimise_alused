"""Encapsulation exercises."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, id, is_active='Active'):
        """Initialize a student object."""
        self.__name = name
        self.__id = id
        self.__is_active = is_active

    def get_id(self):
        """Get the id of the student."""
        return self.__id

    def set_name(self, name):
        """Set the name of the student."""
        self.__name = name

    def get_name(self):
        """Get the name of the student."""
        return self.__name

    def set_status(self, status):
        """Set the status of the student. Valid statuses are: Active, Expelled, Finished, Inactive."""
        valid_statuses = ['Active', 'Expelled', 'Finished', 'Inactive']

        if status not in valid_statuses:
            return
        else:
            self.__is_active = status

    def get_status(self):
        """Get the status of the student."""
        return self.__is_active
