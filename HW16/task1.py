class Person:

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age


class Student(Person):

    def __init__(self, name, last_name, age, average_grade_point, course):
        super().__init__(name, last_name, age)
        self.average_grade_point = average_grade_point
        self.course = course


class Teacher(Person):
    def __init__(self, name, last_name, age, salary, work_experience):
        super().__init__(name, last_name, age)
        self.salary = salary
        self.work_experience = work_experience


teacher_1 = Teacher("Ann", "lastova", 25, 6500, 15)
student_1 = Student("Ivan", "Ivanov", 18, 4.5, 3)
print(teacher_1.salary)
print(student_1.course)
