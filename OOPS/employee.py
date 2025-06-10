class Employee:

    def set_employee(self,name,dept,salary):

        self.name = name

        self.dept = dept

        self.salary = salary

    def get_name(self):
        print(self.name,self.dept,self.salary)


emp_instance1= Employee()


emp_instance1.set_employee("bagio","developer",3000000)

emp_instance1.get_name()

