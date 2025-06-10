class Student:

    def __init__(self,name,roll,course):

        self.name = name

        self.roll = roll

        self.course = course

    def display_student(self):
        print(self.name,self.roll,self.course)


student_instance1 = Student("bagio",17630,"B")
student_instance1.display_student()

student_instance2 = Student("Ron",176300,"A")
student_instance2.display_student()
