class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def show_person(self):
		print("name :",self.name)
		print("age :",self.age)
class student(person):
	def __init__(self,name,age,roll):
		super().__init__(name,age)
		self.roll=roll
	def show_student(self):
		print("roll no :"self.roll)
class Engineering(student):

	def __init__(self,name,age,roll,branch):
		super().__init__(name,age,roll)
		self.branch=branch
	def show_engineering(self):
		print("roll no :"self.branch)

