"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student():

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


class CFGStudent(Student):

    def __init__(self, name, age, id, specialisation):
        super(CFGStudent, self).__init__(name, age, id)
        self.specialisation = specialisation

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        del self.subjects[subject]

    def view_all_subjects(self):
        for subject, grade in self.subjects.items():
            print(subject, grade)

    def average_grade(self):
        return sum(self.subjects.values()) / len(self.subjects)


zaynah = CFGStudent('Zaynah', 22, '13ZA', 'software')
zaynah.add_subject('python', 96)
zaynah.add_subject('SQL', 96)
zaynah.add_subject('java', 78)
print("viewing all 3 subjects")
zaynah.view_all_subjects()
print("demo of removing subject of list")
zaynah.remove_subject('java')
zaynah.view_all_subjects()
print(zaynah.average_grade())
