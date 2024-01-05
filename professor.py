from person import Person

class Professor(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.courses = []

    def set_courses(self, course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses
    
    def __str__(self):
        return '{}, {}: {}'.format(self.last_name, self.first_name, self.courses)
    
    #.join([str(i) for i in z]) ------> look up .join

