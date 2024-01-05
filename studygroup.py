class StudyGroup:
    def __init__(self, id = None):
        self.id = id
        self.students = []
        self.courses = []

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_students(self):
        for student in self.students:
            return student.__str__()
    
    def set_students(self, students):
        self.students = students
    
    def add_student(self, student):
        if student:
            if student in self.students:
                print("This student is already in this group")
                return False
            else:
                self.students.append(student)
                self.courses.extend(student.courses)
        else:
            return True

    def remove_student(self, student):
        self.students.remove(student)
    
    def num_student(self):
        return len(self.students)
    
    def get_courses(self):
        course_list = []
        for course in self.courses:
            course_list.append((course.get_course_name()))
        return course_list
    
    def covered_courses(self):
        covered_courses = []
        for student in self.students:
            for course in student.courses:
                if course in self.courses:
                    continue
                else:
                    self.courses.append(course)
                    covered_courses.append(course.get_course_name())
        return covered_courses
        
    
    def is_valid(self):
        if len(self.students) <= 5:
            return True
        else:
            return False
    
    def __str__(self):
        return '{} - covered courses: {}'.format(self.get_students(), self.covered_courses())

