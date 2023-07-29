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

  def rate_lec(self, lecturer, course, grade): #оценки лекторам
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]
    else:
        return 'Ошибка'

  def _average_rating_st(self): #средняя оценка студентов
    grade = []
    for key, value in self.grades.items():
        for num in value:
            grade.append(num)
    average = sum(grade) / len(grade)
    return average

  def __str__(self):
    res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_rating_st():.2f} \nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
    return res

  def __lt__(self, student):
    if not isinstance(student, Student):
        return 'not a Student '
    return self._average_rating_st() < student._average_rating_st()
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #закрепленные курсы
 
class Lecturer(Mentor): #лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def _average_rating_lec(self): #средняя оценка лекторов
        grade = []
        for key, value in self.grades.items():
            for num in value:
                grade.append(num)
        average = sum(grade) / len(grade)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating_lec():.2f}'
        return res
    
    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            return 'not a Lecturer '
        return self._average_rating_lec() < lecturer._average_rating_lec()

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
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

student_1 = Student('Kirill', 'Morozov', 'M')
student_1.finished_courses = ['Git']
student_1.courses_in_progress += ['Python', 'ООП']

student_2 = Student('Morozova', 'Tatyana', 'G')
student_2.finished_courses = ['C++']
student_2.courses_in_progress += ['Python']

students = [student_1, student_2]

lecturer_1 = Lecturer('Elena', 'Nikitina')
lecturer_1.courses_attached = ['Python', 'Git']

lecturer_2 = Lecturer('Oleg', 'Bulygin')
lecturer_2.courses_attached = ['Python', 'Git', 'C++']

lecturers = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Tim', 'Kuk')
reviewer_1.courses_attached = ['Python', 'Git', 'Matem']

reviewer_2 = Reviewer('Stiv', 'Djobs')
reviewer_2.courses_attached = ['Python', 'Git', 'Market']

reviewer = [reviewer_1, reviewer_2]

student_1.rate_lec(lecturer_1, 'Python', 10)
student_2.rate_lec(lecturer_1, 'Python', 8)

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 8)

student_1.rate_lec(lecturer_1, 'Python', 9)
student_1.rate_lec(lecturer_2, 'Python', 8)
student_2.rate_lec(lecturer_2, 'Python', 10)
student_2.rate_lec(lecturer_1, 'Python', 7)

print('Оценки лекторов:')
print()
print('Оценки студентов:')

print('Эксперты:')
print(reviewer_1)
print(reviewer_2)
print()

print('Лекторы:')
print(lecturer_1)
print(lecturer_2)
print()

print('Студенты:')
print(student_1)
print(student_2)
print()

print('Сравнение студентов по средней оценке:')
print(student_1 > student_2)
print('Сравнение лекторов по средней оценке:')
print(lecturer_1 < lecturer_2)
print()

def total_average_for_students(students, course): #средняя оценка по всем студентам
  grade = []
  for student in students:
    if course in student.grades:
      for key, value in student.grades.items():
        if key == course:
          for num in value:
            grade.append(num)
    else:
      return 'Student does not take this course'
  total_average = sum(grade) / len(grade)
  return total_average

def total_average_for_lecturer(lecturers, course): #средняя оценка по всем лекторам
  grade = []
  for lecturer in lecturers:
    if course in lecturer.grades:
      for key, value in lecturer.grades.items():
        if key == course:
          for num in value:
            grade.append(num)
    else:
      return 'Lecturer does not take this course'
  total_average = sum(grade) / len(grade)
  return total_average

print(f'Средняя оценка по всем студентам: {total_average_for_students(students, "Python"):.2f}')
print(f'Средняя оценка по всем лекторам: {total_average_for_lecturer(lecturers, "Python"):.2f}')
 