"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty = Empty()

    # 3 x person usage
    jane = Person()
    jane.firstname = "Jane"
    jane.lastname = "Doe"
    jane.age = 20

    maddie = Person()
    maddie.firstname = "Maddie"
    maddie.lastname = "Perez"
    maddie.age = 18

    ginny = Person()
    ginny.firstname = "Ginny"
    ginny.lastname = "Weasley"
    ginny.age = 21

    print(ginny.firstname)
    print(type(empty))

    # 3 x student usage
    jane = Student()
    jane.firstname = "Jane"
    jane.lastname = "Doe"
    jane.age = 20

    maddie = Student()
    maddie.firstname = "Maddie"
    maddie.lastname = "Perez"
    maddie.age = 18

    ginny = Student()
    ginny.firstname = "Ginny"
    ginny.lastname = "Weasley"
    ginny.age = 21