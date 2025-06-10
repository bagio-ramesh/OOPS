from json import load
file_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\frameworks_json\\frame_works.json"

with open(file_path,"r") as fr:

    data = load(fr)
    print(data)

    for fw in data:
        print(fw.get("name"))

Bad_courses = [fw.get("name") for fw in data if fw.get("trending")==False]
print(Bad_courses)