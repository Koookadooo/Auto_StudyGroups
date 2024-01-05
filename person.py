class Person:
    def __init__(self, lname = None, fname = None):
        self.last_name = lname
        self.first_name = fname
    
    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, lname):
        self.last_name = lname
    
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, fname):
        self.first_name = fname

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)
