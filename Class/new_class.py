class Employee:

    company_name = "Google"

    def __init__(self,name,dep,salary):

        self.name = name

        self.dep = dep

        self.salary = salary

    def display_employee(self):
        print(self.name,self.dep,self.salary)

    @classmethod
    def show_cmpny_name(cls):
        print(cls.company_name)

    
Employee.show_cmpny_name()

employee_instance = Employee("Bagio","Python Developer",3000000)

employee_instance.display_employee()

    