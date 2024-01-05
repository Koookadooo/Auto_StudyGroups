from person import Person
from student import Student
from professor import Professor
from course import Course
from studygroup import StudyGroup
import names
import random

random.seed(0)

class PersonGenerator():

    def generate(self, first_name = None, last_name = None):
        if first_name is None:
            first_name = names.get_first_name()
        if last_name is None:
            last_name = names.get_last_name()
        return Person(fname = first_name, lname = last_name)
    
    
class StudentGenerator(PersonGenerator):

    def __init__(self):
        super()

    def generate_stud(self, fname = None, lname = None):
        if fname == None and lname == None:
            student = self.generate(fname, lname)
            return Student(student.get_last_name(), student.get_first_name())
        else:
            return Student(fname, lname)
    
    
class ProfessorGenerator(PersonGenerator):

    def __init__(self):
        super()

    def generate_prof(self, fname = None, lname = None):
        professor = self.generate(fname, lname)
        return Professor(professor.get_last_name(), professor.get_first_name())
    

class CourseGenerator():

    def generate_course(self, name = None, dept = None, CRN = None, professor = None):

        deptarments = ["CS", "ENG", "COM", "PSY", "BIO"]
        class_names = ["Rubber Ducks", "ChatGPT", "Pillow Talk", "DO Go Chasing Waterfalls", "Mt. Flatchelor", "Pavlov's Dog's Owner", "Code Drunk, Debug Sober", "Sick Melly Bro", "Do You Even Bend?"]

        if name is None:
            name = random.choice(class_names)
        if dept is None:
            dept = random.choice(deptarments)
        if CRN is None:
            CRN = random.randint(100,400)
        if professor is None:
            professor = ProfessorGenerator().generate_prof()
        
        return Course(name, dept, CRN, professor)