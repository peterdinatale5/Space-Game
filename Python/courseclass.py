class Student:

	def __init__(self, name, age, grade):
		self.name = name #attribute
		self.age = age
		self.grade = grade

	def get_grade(self):
		return self.grade

class Course:

	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def get_name(self):
		return self.name

	def add_student(self, student):
		self.student = student
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False

	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()

		return value / len(self.students)
		

s1 = Student("tim", 15, 95) #class 1 student parameter
s2 = Student("bell", 15, 75)
s3 = Student("jim", 15, 85)

bio = Course("bio", 5)

course = Course("science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_average_grade())
print(s1.get_grade())
print(s2.get_grade())
print(bio.get_name())


