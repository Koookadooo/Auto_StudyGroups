from person import Person
from student import Student
from studygroup import StudyGroup
from course import Course
from professor import Professor
from generators import *
from functions import *
import random


def main():
    random.seed(0)

    stud_generator(500)
    course_generator(15)
    assign_courses(4)

    random_groups(len(students), 5, 2)

    unsatisfied, overly_filled, pct_satisifed = check_correct(study_groups)

    unsatisfied_names = []
    for student in unsatisfied:
        unsatisfied_names.append(student.get_full_name())
    print("\nRANDOM RESULTS: ")
    print("\nUnsatisfied students optimized *random*:")
    print(unsatisfied_names)
    print("\nOver-filled groups optimized *random*:")
    print(overly_filled)
    print("\nPercentage of satisfied students optimized *random*:")
    print(pct_satisifed)

    goal = 0.99
    optimized_groups(unsatisfied, study_groups, pct_satisifed, goal)

    unsatisfied, overly_filled, pct_satisifed = check_correct(study_groups)

    unsatisfied_names = []
    for student in unsatisfied:
        unsatisfied_names.append(student.get_full_name())
    print("\n\n\nOPTIMIZED RESULTS: ")
    print("\nUnsatisfied students *optimized*:")
    print(unsatisfied_names)
    print("\nOver-filled groups *optimized*:")
    print(overly_filled)
    print("\nPercentage of satisfied students *optimized*:")
    print(pct_satisifed)

if __name__ == "__main__":
    main()