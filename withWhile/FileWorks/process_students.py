all_students_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\all_students.txt"

passed_students_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\passed_students.txt"

all_students = set()

passed_students = set()

with open(all_students_path,"r") as fr:
    for name in fr:
        all_students.add(name.rstrip("\n"))

with open(passed_students_path,"r") as fr1:
    for name in fr1:
        passed_students.add(name.rstrip("\n"))

failed_students = all_students.difference(passed_students)
print(failed_students)