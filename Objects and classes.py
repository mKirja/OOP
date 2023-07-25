
class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
 
  def add_courses(self, course_name):
    self.finished_courses.append(course_name)

  def rate_lec(self, lecturer, course, grade): #оценки леторам
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]
    else:
        return 'Ошибка'
 
     
class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = [] #закрепленные курсы
 
class Lecturer(Mentor): #лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor): #эксперты
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade): #оценки студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
best_student.rate_lec(cool_mentor, 'Python', 10)
best_student.rate_lec(cool_mentor, 'Python', 9)
best_student.rate_lec(cool_mentor, 'Python', 10)
 
print(cool_mentor.grades)