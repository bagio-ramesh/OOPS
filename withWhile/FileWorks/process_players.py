march_1_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\01_march_31_contribution.txt"
april_2_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\02_april_2.txt"
april_3_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\03_april_07.txt"

new_dicts = {}

with open(march_1_path,"r") as fr,open(april_2_path,"r") as fr1,open(april_2_path,"r") as fr2:
    tottal_value = [fr,fr1,fr2]
    
    for item in tottal_value:
        for line in item:
            line = line.strip()
            splited = line.split(",")
            name = splited[0]
            amount = int(splited[1])

            if name not in new_dicts:
                new_dicts[name] = amount

            else:
                new_dicts[name] += amount

print(new_dicts)

high = max(new_dicts,key=new_dicts.get)
print(high,"=",new_dicts.get(high))
low = min(new_dicts,key=new_dicts.get)
print(low,"=",new_dicts.get(low))


