employees=[
    {"id":100,"name":"hari","department":"hr","salary":24000,"location":"ekm"},
    {"id":101,"name":"vipin","department":"hr","salary":34000,"location":"ekm"},
    {"id":102,"name":"james","department":"ba","salary":54000,"location":"tvm"},
    {"id":103,"name":"Bajio","department":"ba","salary":223000,"location":"bnr"},
    {"id":104,"name":"james","department":"qa","salary":27000,"location":"tvm"},
    {"id":105,"name":"das","department":"qa","salary":34000,"location":"tsr"},

]

# # total number of employees

# employee_count=len(employees)
# print(employee_count)

# # dispaly name of all employees

# for emp in employees:
#     print(emp.get("name"))

# for emp in employees:
#     print(emp.get("salary"))

# hr_employee = [emp.get("name")for emp in employees if emp.get("department")=="hr"]
# print(hr_employee)

# salary_fltr = [emp.get("name") for emp in employees if emp.get("salary") > 30000 ]
# print(salary_fltr)


def get_emp_sal(dictinary):
    return dictinary.get("salary")

highest_sal = max(employees,key=get_emp_sal)
print(highest_sal)


min_sal = min(employees,key=get_emp_sal)
print(min_sal)

sorted_employees = sorted(employees,key=get_emp_sal,reverse=True)
print(sorted_employees)


sum_of_salary =[emp.get("salary") for emp in employees]
print(sum(sum_of_salary))