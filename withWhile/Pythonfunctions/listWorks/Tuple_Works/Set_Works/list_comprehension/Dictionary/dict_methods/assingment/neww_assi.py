employees={
    "ram":34000,
    "ravi":25000,
    "vipin":18000,
    "vijay":28000,
    "ahana":45000
}

# lamda key:employees.get(key)

# max_salary = max(employees,key = lamda employees:employees.get(key))
# print(max_salary,employees.get(max_salary))

# min_salary = min(employees,key = lamda employees:employees.get(key)) )
# print(min_salary,employees.get(min_salary))

# sorted_employees = sorted(employees,key= lamda key:employees.get(key)))
# print(sorted_employees)
 
tottal = [sal for sal in employees.values()]

print(sum(tottal))