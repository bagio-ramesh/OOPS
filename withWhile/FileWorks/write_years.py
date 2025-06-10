file_path = open("C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\all_years.txt","w")

for year in range(1980,2026):
    file_path.write(str(year)+"\n")
