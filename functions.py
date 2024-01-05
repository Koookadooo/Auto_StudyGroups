from person import Person
from student import Student
from studygroup import StudyGroup
from course import Course
from professor import Professor
from generators import *
import random

random.seed(0)

students = []
courses = []
study_groups = []

#Generates a stud
def stud_generator(num_to_gen = None):
    stud_generator = StudentGenerator()
    for i in range(0,num_to_gen):
        students.append(stud_generator.generate_stud())

#Generates a course
def course_generator(num_to_gen = None):
    course_generator = CourseGenerator()
    for i in range(0,num_to_gen):
        courses.append(course_generator.generate_course())

#Generates a professor
def assign_courses(num_to_assign = None):
    for student in students:
        while len(student.courses) < num_to_assign:
            student.add_courses(random.choice(courses))
        for course in student.courses:
            course.add_student(student)

"""Function calculates the number of study groups then iterates through and creates a group for each iteration in number of study groups.
for each group created iterate through the maximum number of students in a group and assign a random students to that group. Make sure the rnadom student
is not in current group already and doesn't belong to 2 or more groups. Counter to catch circumstance that last person was not assigned until the last group
and terefore will not meet the checks for not belonging to the same group."""
def random_groups(total_students = 500, max_group_size = 5, max_student_groups = 2):
    num_study_groups = (total_students * max_student_groups) // max_group_size  
    for i in range(0, num_study_groups):
        study_group = StudyGroup()
        study_group.set_id(i)
        j = max_group_size
        counter = 0
        while j > 0:
            student = random.choice(students)
            if student not in study_group.students and len(student.study_groups) < 2:
                student.add_groups(study_group)
                j -= 1
                counter+=1
                if counter>=total_students-1:
                    break
            else:
                continue
        study_groups.append(study_group)


"""Function takes our list of unsatisfied students, the list of study groups, current percent of satisfied students, and our goal satisfaction rate. 
Uses a for loop to iterate through our list of unsaisfied students and switch the first study group of the student we are looking at with the first study group of the next student.
Calls check correct to on new study_group set and returns new list of unsatisfied students and percent or satisfied students. These then get fed back into the while and for loops
to run until we reach our goal percentage. """
def optimized_groups(unsat_students, study_groups, percent_sat, goal):
    while percent_sat < goal:
        for i in range(len(unsat_students)-1):
            unsat_students[i].study_groups[0], unsat_students[i+1].study_groups[0] = unsat_students[i+1].study_groups[0], unsat_students[i].study_groups[0]
        unsat_students, bloated_groups, percent_sat = check_correct(study_groups)

    
        
"""Function initializes empty array to fill and return. Iterates through each study group, the students in those study groups,and check if student has valid 
group. If yes, append to satisfied students, if no, append to unsatisfied students. If group has more than 5 students,append group to full study group."""
def check_correct(studygroups):
    unsat_students = []
    sat_students=[]
    full_sg = []
    for sg in studygroups:
        for student in sg.students:
            if student.v_group(2):
                if student not in sat_students:
                    sat_students.append(student)
            else:
                if student not in unsat_students:
                    unsat_students.append(student)
        if not sg.is_valid():
            full_sg.append(sg)
        else:
            continue
    return unsat_students, full_sg, len(sat_students)/(len(unsat_students)+len(sat_students))