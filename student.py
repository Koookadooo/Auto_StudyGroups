from person import Person

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.courses = []
        self.study_groups = []

    def get_full_name(self):
        return super().__str__()

    def set_courses(self, courses):
        if courses.__class__ == list:
            self.courses = courses
        else:
            lst_courses = []
            lst_courses.append(courses)
            self.courses = lst_courses

    def get_courses(self):
        course_list = []
        for course in self.courses:
            course_list.append((course.get_course_name()))
        return course_list
    
    def add_courses(self, course):
        if course in self.courses:
            return
        else:
            self.courses.append(course)
    
    def v_courses(self, x):
        courses_set = set(self.courses)
        if len(courses_set) < len(self.courses) or len(self.courses) > x:
            return False
        else:
            return True
    
    def set_groups(self, groups):
        if groups.__class__ == list:
            self.groups = groups
        else:
            lst_groups = []
            lst_groups.append(groups)
            self.groups = lst_groups
    
    def get_groups(self):
        groups_list = []
        for sg in self.study_groups:
            groups_list.append(sg.get_id())
        return groups_list
    
    def add_groups(self, group):
        if group in self.study_groups:
            print("already in that group")
            return False
        else:
            self.study_groups.append(group)
            group.add_student(self)
    
    def v_group(self, num_groups = 2):
        if len(self.study_groups) <= num_groups:
            for course in self.courses:
                is_valid = False
                for student in course.roster:
                    if student == self:
                        continue
                    else:
                        for group in student.study_groups:
                            if group in self.study_groups:
                                is_valid = True
                                break
                    if is_valid:
                        break
                if not is_valid:
                    return False
            if is_valid:
                return True
            else:
                return False
        else:
            return False    
            
    def __str__(self):
        return '{}, {}: {}'.format(self.last_name, self.first_name, self.get_courses())
    
