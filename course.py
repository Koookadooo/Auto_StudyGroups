class Course:
    def __init__(self, name = None, dept = None, CRN = None, professor = None):
        self.course_name = name
        self.department = dept
        self.course_number = CRN
        self.professor = professor
        self.roster = []
    
    def get_course_name(self):
        return self.course_name
    
    def set_course_name(self, name):
        self.course_name = name
    
    def get_department(self):
        return self.department
    
    def set_department(self, dept):
        self.department = dept

    def get_course_number(self):
        return self.course_number
    
    def set_course_number(self, CRN):
        self.course_number = CRN
    
    def get_professor(self):
        return self.professor
    
    def set_professor(self, professor):
        self.professor = professor

    def get_roster(self):
        return self.roster
    
    def set_roster(self, roster):
        self.roster = roster

    def add_student(self, student):
        self.roster.append(student)
    
    def remove_student(self, student):
        self.roster.remove(student)

    def is_valid(self):
        if (self.professor == None) or (len(self.roster) < 2):
            return False
        else:
            return True
    
    def __str__(self):
        return '({}, {}, {}) Professor - {}. {} students enrolled'.format(self.department, self.course_name, self.course_number, self.professor, len(self.roster))
