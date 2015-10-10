class Transcript(object):
    """
    GPA table
    """
    def __init__(self, *args):
        self._courses = dict()
        self._units_taken = 0
        self._grade_points = 0
        self._gpa = 0
        self._grade_map = {'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1, 'F':0}

        for course,weight,grade in args:
            self.add_course(course, weight, grade)

    def add_course(self,course, weight, grade):
        if course in self._courses.keys():
            old_weight, old_grade = self._courses[course]
            self._units_taken -= old_weight
            self._grade_points -= old_weight * old_grade
        self._courses[course] = (weight,grade)
        self._update_gpa(course,weight,grade)        

    def _update_gpa(self,course,weight,grade):
        self._units_taken += weight
        self._grade_points += weight * self._grade_map[grade]
        self._gpa = self._grade_points / self._units_taken

    def gpa(self):
        return float(self._gpa)

    def courses(self):
        return dict(self._courses)

def get_input(tran):
    loop = True
    while loop:
        course = input("Course name: ")
        weight = float(input("Course weight: "))
        grade = input("Course grade: ")
        tran.add_course(course,weight,grade)
        cont = input("Add another course? ([Y]/N):")
        try:
            if cont[0].lower() == 'y':
                loop = True
            else:
                loop = False
        except:
            loop = True

if __name__ == '__main__':
    t = Transcript()
    get_input(t)
    print("\n")
    print("Course\t\tWeight\t\tGrade\n")
    for k,v in t.courses().items():
        print("{}\t{}\t\t{}\n".format(k,v[0],v[1]))
    print("GPA: {}\n".format(t.gpa()))






