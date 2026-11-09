class School:
    def __init__(self):
        """Dictionary of grades and students"""
        self._grades = {}

        """Set of names"""
        self._students = set()

        """Value of if added or not"""
        self._added = []

    def add_student(self, name, grade):
        if name in self._students:
            self._added.append(False)
            return
            
        self._students.add(name)
        if grade not in self._grades:
            self._grades[grade] = []

        self._grades[grade].append(name)
        self._added.append(True)
        
    def roster(self):
        students_in_school = []
        for grade in sorted(self._grades.keys()):
            students_in_school.extend(sorted(self._grades[grade]))
        return students_in_school
        

    def grade(self, grade_number):
        return sorted(self._grades.get(grade_number, []))
        

    def added(self):
        return self._added
