class Student:
    def __init__(self, email, name, surname, all_grade=None, status=None):
        if all_grade is None:
            self.all_grade = {
            "project": -1,
            "l_1": -1,
            "l_2": -1,
            "l_3": -1,
            "h_1": -1,
            "h_2": -1,
            "h_3": -1,
            "h_4": -1,
            "h_5": -1,
            "h_6": -1,
            "h_7": -1,
            "h_8": -1,
            "h_9": -1,
            "h_10": -1,
            "grade": -1,
            }
        else:
            self.all_grade = all_grade
        self.email = email
        self.name = name
        self.surname = surname
        if status is None:
            self.status = None
        else:
            self.status = status

    # def __str__(self):    return str(self.email) + " , " + str(self.name) + " , " + str(self.surname) + " , " + str(
    #    self.status) + " , " + str(self.all_grade)

    def __repr__(self):
       return f"Student(email='{self.email}', name = '{self.name}', surname = '{self.surname}', " \
        f"all_grade = {self.all_grade}, status = {self.status})"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.email == other.email

    @staticmethod
    def compareStudentsNames(x,y):
       return x.name >= y.name

    @staticmethod
    def compareStudentsSurnames(x,y):
       return x.surname >= y.surname

    def getPersonalData(self):
       return self.email,self.name,self.surname

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __le__(self, other):
        return self.name <= other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __ne__(self, other):
        return self.name <= other.name
