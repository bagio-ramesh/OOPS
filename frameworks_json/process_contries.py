from json import load

file_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\frameworks_json\\contries.json"

def get_population(dicts):
    return dicts.get("population")

with open(file_path,"r",encoding="utf-8") as fr1:
    data = load(fr1)
    

all_contries_name = [contry.get("name") for contry in data]
# print("All Contries:",all_contries_name)

most_populated_contry = max(data,key=get_population)
# print("Most populated Contry:",most_populated_contry.get("name"))

least_populated_contry = min(data,key=get_population)
# print("Least populated Contry:",least_populated_contry.get("name"))

independent_contries = [contry.get("name") for contry in data if contry.get("independent")== True]
# print("Independent contries:",independent_contries)

all_regions = {contry.get("region") for contry in data}
# print("All Regions:",all_regions)

asian_contries = [contry.get("name") for contry in data if contry.get("region")=="Asia"]
# print("Asian Contries:",asian_contries)

indian_borders = [contry.get("borders") for contry in data if contry.get("name")=="India"]
# print("Indian Borders:",indian_borders)

